import os
import pandas as pd
import xml.etree.ElementTree as ET
import re
from config import report_configs, namespaces

def get_report_type_from_descriptor(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    ns = namespaces
    descriptors = root.findall('.//ss:Cell/ss:Data', namespaces=ns)
    found_descriptors = []

    for data in descriptors:
        if data.text:
            text = data.text.strip()
            found_descriptors.append(text)
            for report_type, config in report_configs.items():
                descriptor = config.get('descriptor')
                if descriptor and descriptor.strip().lower() == text.strip().lower():
                    print(f"Matched report type '{report_type}' for descriptor '{text}' in file {os.path.basename(xml_file)}")
                    return report_type
    print(f"No matching descriptor found in {os.path.basename(xml_file)}. Descriptors found: {found_descriptors}")
    return None

def parse_xml(xml_file, report_type):
    config = report_configs[report_type]
    headers = config['headers']
    exclusions = config.get('exclusions', [])
    tree = ET.parse(xml_file)
    root = tree.getroot()
    ns = namespaces
    rows = root.findall('.//ss:Row', namespaces=ns)
    parsed_data = []
    header_found = False
    header_indices = []
    portfolio_return_row = None
    portfolio_name = "Unknown Portfolio"
    portfolio_date = "Unknown Date"

    # Extract portfolio name and date from the XML
    for data in root.findall('.//ss:Data', namespaces=ns):
        text_content = data.text.strip() if data.text else ""
        if text_content.startswith("Meridian") or text_content.startswith("G "):
            portfolio_name = text_content
        if re.match(r'\d{4}-\d{2}-\d{2}', text_content):
            portfolio_date = text_content

    for idx, row in enumerate(rows):
        row_data = []
        cells = row.findall('.//ss:Cell', namespaces=ns)
        for cell in cells:
            data = cell.find('.//ss:Data', namespaces=ns)
            value = data.text.strip() if data is not None and data.text else ''
            row_data.append(value)

        if not any(row_data):
            continue

        if any(exclusion in ' '.join(row_data) for exclusion in exclusions):
            print(f"Skipping row due to exclusion: {row_data}")
            continue

        if row_data[0] in ["Aggregate:", "Average:", "Benchmark:"]:
            if report_type.startswith('model_'):
                if idx + 1 < len(rows):
                    next_row = rows[idx + 1]
                    next_row_data = []
                    next_cells = next_row.findall('.//ss:Cell', namespaces=ns)
                    for cell in next_cells:
                        data = cell.find('.//ss:Data', namespaces=ns)
                        value = data.text.strip() if data else ''
                        next_row_data.append(value)

                    if len(next_row_data) > 0 and next_row_data[0] == "-":
                        next_row_data[0] = portfolio_name
                        next_row_data[1] = portfolio_date
                    while len(next_row_data) < len(headers):
                        next_row_data.append('')
                    if len(next_row_data) > len(headers):
                        next_row_data = next_row_data[:len(headers)]
                    portfolio_return_row = next_row_data
            continue

        if not header_found:
            normalized_row = [re.sub(r'\W+', '', cell.lower().strip()) for cell in row_data]
            normalized_headers = [re.sub(r'\W+', '', header.lower().strip()) for header in headers]
            match_threshold = 0.8
            matched_headers = [header for header in normalized_headers if header in normalized_row]
            if len(matched_headers) / len(normalized_headers) >= match_threshold:
                header_found = True
                print(f"Header found in {os.path.basename(xml_file)}")
                header_indices = [normalized_row.index(header) for header in matched_headers]
                continue
        elif header_found:
            row_aligned = [row_data[i] if i < len(row_data) else '' for i in header_indices]
            if len(row_aligned) != len(headers):
                print(f"Row length mismatch in {os.path.basename(xml_file)}: Expected {len(headers)}, got {len(row_aligned)}")
                continue
            parsed_data.append(row_aligned)

    if not header_found:
        print(f"No header found in {os.path.basename(xml_file)}")

    return headers, parsed_data, portfolio_return_row

def process_files(directory):
    dataframes = {}
    for filename in os.listdir(directory):
        if filename.endswith('.xls'):
            filepath = os.path.join(directory, filename)
            report_type = get_report_type_from_descriptor(filepath)

            if report_type not in ["model_compare", "model_annual"]:
                print(f"Skipping file {filename} because report type '{report_type}' is not 'model_compare' or 'model_annual'")
                continue

            headers, parsed_data, portfolio_return_row = parse_xml(filepath, report_type)
            if not parsed_data and not portfolio_return_row:
                print(f"No data found in {filename}")
                continue
            df = pd.DataFrame(parsed_data, columns=headers)
            df['report_type'] = report_type
            if portfolio_return_row:
                portfolio_return_row_with_type = portfolio_return_row + [report_type]
                portfolio_df = pd.DataFrame([portfolio_return_row_with_type], columns=df.columns)
                df = pd.concat([df, portfolio_df], ignore_index=True)
            if report_type in dataframes:
                dataframes[report_type] = pd.concat([dataframes[report_type], df], ignore_index=True)
            else:
                dataframes[report_type] = df
    return dataframes

def combine_dataframes(dataframes):
    model_compare_dfs = []
    model_annual_dfs = []

    for report_type, df in dataframes.items():
        if report_type == 'model_compare':
            model_compare_dfs.append(df)
        elif report_type == 'model_annual':
            model_annual_dfs.append(df)

    model_compare_df = pd.concat(model_compare_dfs, ignore_index=True) if model_compare_dfs else pd.DataFrame()
    model_annual_df = pd.concat(model_annual_dfs, ignore_index=True) if model_annual_dfs else pd.DataFrame()

    return model_compare_df, model_annual_df

if __name__ == "__main__":
    directory = '/Users/tylermontell/Projects/magic_machine_app/test/test_xls'
    dataframes = process_files(directory)
    model_compare_df, model_annual_df = combine_dataframes(dataframes)

    if not model_compare_df.empty:
        model_compare_df.to_csv('model_compare_data.csv', index=False)
    if not model_annual_df.empty:
        model_annual_df.to_csv('model_annual_data.csv', index=False)

    print("DataFrames have been saved to CSV files.")
