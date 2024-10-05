import xml.etree.ElementTree as ET
import pandas as pd
import os
import re
from config import namespaces, report_configs

# --------------------------- Helper Functions --------------------------- #

def clean_text(text):
    return text.strip() if text else ''

def normalize_text(text):
    """Normalize text for consistent header matching."""
    return re.sub(r'\W+', '', text.lower().strip())

def clean_data(df, exclusions):
    """Clean the dataframe by removing unwanted rows and applying exclusions."""
    # Remove rows where all values are empty, or consist of mostly commas/dashes/nan
    df = df.replace(['-', '', 'nan'], '').dropna(how='all')

    # Remove rows that match known exclusion terms, but don't exclude the header row
    exclusion_pattern = '|'.join([re.escape(exclusion) for exclusion in exclusions])
    df = df[~df.apply(lambda row: row.astype(str).str.contains(exclusion_pattern).any(), axis=1)]

    # Drop any duplicate rows just in case
    df = df.drop_duplicates()

    return df

# --------------------------- Main Processing Functions --------------------------- #

def parse_xml(xml_file, expected_columns, exclusions):
    """Parse XML file and return parsed data based on the expected headers."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    ns = namespaces
    rows = root.findall('.//ss:Row', namespaces=ns)
    parsed_data = []
    header_found = False
    header_indices = []

    normalized_headers = [normalize_text(header) for header in expected_columns]

    for idx, row in enumerate(rows):
        row_data = []
        cells = row.findall('.//ss:Cell', namespaces=ns)
        for cell in cells:
            data = cell.find('.//ss:Data', namespaces=ns)
            value = clean_text(data.text) if data is not None and data.text is not None else ''
            row_data.append(value)

        if not any(row_data):
            continue

        # Identify and capture headers
        if not header_found:
            normalized_row = [normalize_text(cell) for cell in row_data]
            matched_headers = [header for header in normalized_headers if header in normalized_row]
            match_threshold = 0.8
            if len(matched_headers) / len(normalized_headers) >= match_threshold:
                header_found = True
                print(f"Header found in {os.path.basename(xml_file)}: {row_data}")
                header_indices = [normalized_row.index(header) for header in matched_headers]
                continue
        else:
            # Align row data with headers
            row_aligned = [row_data[i] if i < len(row_data) else '' for i in header_indices]
            if len(row_aligned) != len(expected_columns):
                print(f"Row length mismatch in {os.path.basename(xml_file)}: Expected {len(expected_columns)}, got {len(row_aligned)}")
                continue
            parsed_data.append(row_aligned)

    if not header_found:
        print(f"No header found in {os.path.basename(xml_file)}")

    print(f"Headers: {expected_columns}")
    print(f"Parsed Data (first 5 rows): {parsed_data[:5]}")

    return expected_columns, parsed_data

def process_files(directory, report_type):
    """Process all files in the directory and parse data based on the report type."""
    dataframes = []
    config = report_configs[report_type]
    expected_columns = config['headers']
    exclusions = config.get('exclusions', [])

    for filename in os.listdir(directory):
        if filename.endswith('.xls'):
            filepath = os.path.join(directory, filename)
            headers, parsed_data = parse_xml(filepath, expected_columns, exclusions)
            if not parsed_data:
                print(f"No data found in {filename}")
                continue
            
            # Create a new DataFrame for the parsed data
            df = pd.DataFrame(parsed_data, columns=headers)

            # Clean the DataFrame before further processing
            df = clean_data(df, exclusions)
            
            # Add to the list of DataFrames
            dataframes.append(df)
    
    return dataframes

# --------------------------- DataFrame Combination --------------------------- #

def combine_dataframes(dataframes):
    """Combine all dataframes."""
    combined_df = pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()
    return combined_df

# --------------------------- Main Function --------------------------- #

def process_and_save_data(directory, report_type):
    """Process all files and save the combined data to CSV."""
    # Process all files in the directory and combine them into a single DataFrame
    dataframes = process_files(directory, report_type)
    combined_df = combine_dataframes(dataframes)
    
    if not combined_df.empty:
        output_file = '/Users/tylermontell/Projects/magic_machine_app/test/basics_output.csv'
        combined_df.to_csv(output_file, index=False)
        print(f"Combined DataFrame has been cleaned, processed, and saved to {output_file}.")
    else:
        print("No data to process.")

# --------------------------- Script Execution --------------------------- #

if __name__ == "__main__":
    directory = '/Users/tylermontell/Projects/magic_machine_app/test/test_xls'
    process_and_save_data(directory, 'model_basics')
