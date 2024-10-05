import xml.etree.ElementTree as ET
import pandas as pd
import os
import re
from config import report_configs, namespaces, fund_expected_columns, etf_expected_columns


# --------------------------- Helper Functions --------------------------- #

def clean_text(text):
    return text.strip() if text else ''


def normalize_text(text):
    """Normalize text for consistent header matching."""
    return re.sub(r'\W+', '', text.lower().strip())


def append_portfolio_return_row(df, portfolio_return_row):
    """Append the portfolio return row to the DataFrame if it exists."""
    if len(portfolio_return_row) < len(df.columns):
        portfolio_return_row += [''] * (len(df.columns) - len(portfolio_return_row))
    elif len(portfolio_return_row) > len(df.columns):
        portfolio_return_row = portfolio_return_row[:len(df.columns)]
    
    portfolio_df = pd.DataFrame([portfolio_return_row], columns=df.columns)
    return pd.concat([df, portfolio_df], ignore_index=True)

def clean_data(df):
    # Remove rows where all values are empty, or consist of mostly commas/dashes
    df = df.replace(['-', '', 'nan'], '').dropna(how='all')
    
    # Remove rows with placeholder content (e.g., repeated commas)
    df = df[df.apply(lambda row: not all(cell in ['', '-'] for cell in row), axis=1)]
    
    # Drop rows that start with unwanted values like "S&P 500 TR USD" or "Morningstar"
    if 'Name' in df.columns:
        df = df[~df['Name'].str.contains("S&P 500 TR USD|Morningstar", na=False)]
    
    # Drop any duplicate rows just in case
    df = df.drop_duplicates()

    return df

def format_date_column(date_str):
    """
    Detects and formats date strings in 'YYYYMMDD' format to 'YYYY-MM-DD'.
    """
    # Check if the string is 8 digits long (matches 'YYYYMMDD' pattern)
    if re.match(r'^\d{8}$', str(date_str)):
        return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
    return date_str

# --------------------------- Main Processing Functions --------------------------- #

def get_report_type_from_descriptor(xml_file):
    """Determine report type by inspecting the XML file descriptors."""
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
    """Parse XML file based on report type and return parsed data."""
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

    normalized_headers = [normalize_text(header) for header in headers]

    for idx, row in enumerate(rows):
        row_data = []
        cells = row.findall('.//ss:Cell', namespaces=ns)
        for cell in cells:
            data = cell.find('.//ss:Data', namespaces=ns)
            value = clean_text(data.text) if data is not None and data.text is not None else ''
            row_data.append(value)

        if not any(row_data):
            continue

        # Skip excluded rows
        if any(exclusion in ' '.join(row_data) for exclusion in exclusions):
            print(f"Skipping row due to exclusion: {row_data}")
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
            if len(row_aligned) != len(headers):
                print(f"Row length mismatch in {os.path.basename(xml_file)}: Expected {len(headers)}, got {len(row_aligned)}")
                continue
            parsed_data.append(row_aligned)

    if not header_found:
        print(f"No header found in {os.path.basename(xml_file)}")

    print(f"Headers: {headers}")
    print(f"Parsed Data (first 5 rows): {parsed_data[:5]}")

    return headers, parsed_data, None

def process_files(directory, report_type_filter=None):
    dataframes = {}
    
    for filename in os.listdir(directory):
        if filename.endswith('.xls'):
            filepath = os.path.join(directory, filename)
            report_type = get_report_type_from_descriptor(filepath)
            
            # Apply filtering if specific report types are being targeted
            if report_type_filter and report_type not in report_type_filter:
                continue

            if report_type is None:
                print(f"Could not determine report type for {filename}")
                continue

            headers, parsed_data, portfolio_return_row = parse_xml(filepath, report_type)
            if not parsed_data and not portfolio_return_row:
                print(f"No data found in {filename}")
                continue
            
            # Create a new DataFrame for the parsed data
            df = pd.DataFrame(parsed_data, columns=headers)
            df['report_type'] = report_type
            
            # Clean the DataFrame before further processing
            df = clean_data(df)
            
            # Collect DataFrames based on the type of report
            dataframes[report_type] = pd.concat([dataframes.get(report_type, pd.DataFrame()), df], ignore_index=True)
    
    return dataframes

def ensure_correct_column_alignment(df, expected_columns):
    """
    Ensure the dataframe columns align with the expected columns, filling missing columns with empty strings.
    Columns not in expected_columns will be removed.
    """
    # Reindex the dataframe with the expected columns. If some columns are missing, they will be added with empty values.
    df = df.reindex(columns=expected_columns, fill_value='')

    # Drop rows where all values are empty
    df = df.dropna(how='all')

    # Check if 'Name' and 'Ticker' columns exist before dropping duplicates
    if 'Name' in df.columns and 'Ticker' in df.columns:
        df = df.drop_duplicates(subset=['Name', 'Ticker'], keep='first')

    return df

# --------------------------- DataFrame Combination --------------------------- #

def combine_fund_dataframes(dataframes):
    """Combine all fund-related dataframes."""
    fund_dfs = [df for report_type, df in dataframes.items() if report_type.startswith('fund_')]
    funds_df = pd.concat(fund_dfs, ignore_index=True) if fund_dfs else pd.DataFrame()
    funds_df = clean_data(funds_df)
    return ensure_correct_column_alignment(funds_df, fund_expected_columns)


def combine_etf_dataframes(dataframes):
    """Combine all ETF-related dataframes."""
    etf_dfs = [df for report_type, df in dataframes.items() if report_type.startswith('etf_')]
    etfs_df = pd.concat(etf_dfs, ignore_index=True) if etf_dfs else pd.DataFrame()
    etfs_df = clean_data(etfs_df)
    return ensure_correct_column_alignment(etfs_df, etf_expected_columns)


# --------------------------- Main Function --------------------------- #

def remove_empty_rows_between_files(df):
    # Remove fully empty rows that may exist between separate files (Funds and ETFs)
    df = df.dropna(how='all')  # Drop rows where all values are empty
    return df

def process_fund_and_etf_dataframes(dataframes):
    # Process Fund Data
    funds_df = combine_fund_dataframes(dataframes)
    if not funds_df.empty:
        funds_df = remove_empty_rows_between_files(funds_df)
        funds_df.to_csv('funds_data.csv', index=False)
        print("Fund DataFrame has been cleaned, processed, and saved to funds_data.csv.")
    
    # Process ETF Data
    etfs_df = combine_etf_dataframes(dataframes)
    if not etfs_df.empty:
        etfs_df = remove_empty_rows_between_files(etfs_df)
        etfs_df.to_csv('etfs_data.csv', index=False)
        print("ETF DataFrame has been cleaned, processed, and saved to etfs_data.csv.")

# --------------------------- Script Execution --------------------------- #

if __name__ == "__main__":
    directory = '/Users/tylermontell/Projects/magic_machine_app/test/test_xls'
    dataframes = process_files(directory)
    process_fund_and_etf_dataframes(dataframes)