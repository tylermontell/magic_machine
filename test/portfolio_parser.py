import pandas as pd
import os
from lxml import etree as ET
import re

# Namespace for XML
namespaces = {'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}

# Clean and prepare the text
def clean_text(text):
    return text.strip() if text else ''

# Detect portfolio name based on specific patterns
def detect_portfolio_name(row):
    for cell in row:
        if cell.startswith("G ") or cell.startswith("Meridian"):
            return cell
    return None

# Combine portfolio names with their data rows
def combine_portfolio_and_data(rows):
    combined_rows = []
    skip_next = False

    for idx, row in enumerate(rows):
        if not skip_next:
            portfolio_name = detect_portfolio_name(row)
            if portfolio_name and idx + 1 < len(rows):
                combined_row = [portfolio_name] + rows[idx + 1][1:]
                combined_rows.append(combined_row)
                skip_next = True  # Skip the next row as it's been merged
            else:
                combined_rows.append(row)
        else:
            skip_next = False  # Reset skip
    return combined_rows

# Process the XML rows
def process_rows(root):
    rows = root.xpath('//ss:Row', namespaces=namespaces)
    extracted_rows = []

    for row in rows:
        row_data = [clean_text(cell.text) for cell in row.xpath('ss:Cell/ss:Data', namespaces=namespaces)]
        if row_data and not re.match(r"Aggregate:", row_data[0]):
            extracted_rows.append(row_data)

    return extracted_rows

# Adjust row to match expected column count (either truncate or pad with empty values)
def adjust_row_length(row, expected_length):
    if len(row) > expected_length:
        return row[:expected_length]  # Truncate to expected length
    elif len(row) < expected_length:
        return row + [''] * (expected_length - len(row))  # Pad with empty strings
    return row

# Process files and create CSV
def process_files(directory):
    all_data = []

    for filename in os.listdir(directory):
        if filename.endswith('.xls'):
            filepath = os.path.join(directory, filename)
            tree = ET.parse(filepath)
            root = tree.getroot()

            # Extract and clean rows
            extracted_rows = process_rows(root)
            combined_rows = combine_portfolio_and_data(extracted_rows)

            # Append to final data, adjusting row length to match header count
            for row in combined_rows:
                all_data.append(adjust_row_length(row, 12))  # Adjust rows to 12 columns

    # Create a DataFrame and save to CSV
    headers = ['Name', 'Morningstar Category', 'Mkt Annl Return 2014', 'Mkt Annl Return 2015', 'Mkt Annl Return 2016', 'Mkt Annl Return 2017', 'Mkt Annl Return 2018', 'Mkt Annl Return 2019', 'Mkt Annl Return 2020', 'Mkt Annl Return 2021', 'Mkt Annl Return 2022', 'Mkt Annl Return 2023']
    df = pd.DataFrame(all_data, columns=headers)
    df.to_csv('cleaned_portfolio_data.csv', index=False)

# Run the process
if __name__ == "__main__":
    directory = '/Users/tylermontell/Projects/magic_machine_app/test/test_xls'
    process_files(directory)
