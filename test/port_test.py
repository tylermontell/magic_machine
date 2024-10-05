import os
from lxml import etree
import csv
from datetime import datetime
from config import report_configs, namespaces

# Step 1: Define the input directory and output file
input_directory = '/Users/tylermontell/Projects/magic_machine_app/test/test_xls'
output_file_path = '/Users/tylermontell/Projects/magic_machine_app/test/test_xls/filtered_data_output.csv'

# Step 2: Define XML namespaces
namespaces = {
    'ss': 'urn:schemas-microsoft-com:office:spreadsheet'
}

# Step 3: Helper function to parse date strings
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None

# Step 4: Function to clean text by removing excluded characters
def clean_text(text):
    for char in excluded_characters:
        text = text.replace(char, '')
    return text

# Step 5: Function to process each individual file
def process_file(file_path):
    with open(file_path, 'rb') as file:
        xml_data = file.read()
    
    # Parse the XML file using the etree module
    root = etree.fromstring(xml_data)

    # Initialize variables to capture key information
    portfolio_name = "Unknown Portfolio Name"  # Will be updated once the portfolio name is detected
    fund_rows = []  # List to store fund rows (e.g., those containing 'Vanguard')
    portfolio_return_row = None  # Will hold the row for the portfolio return
    most_recent_return_date_str = None  # Store the most recent date as a string
    most_recent_return_date_obj = None  # Store the most recent date as a datetime object

    # Detect the portfolio name (Meridian or G Portfolio)
    for data in root.xpath('//ss:Data', namespaces=namespaces):
        text_content = data.text.strip() if data.text else ''
        if text_content.startswith("Meridian") or text_content.startswith("G "):
            portfolio_name = text_content
            break  # Stop once the portfolio name is found

    # Extract fund rows and locate the "Aggregate:" row
    rows = root.xpath('//ss:Row', namespaces=namespaces)
    aggregate_found = False

    # Iterate through each row to gather data and locate the "Aggregate:" row
    for idx, data in enumerate(rows):
        row_data = [clean_text(d.text.strip() if d.text else '') for d in data.xpath('ss:Cell/ss:Data', namespaces=namespaces)]
        
        # Skip empty rows
        if not row_data:
            continue

        # Check if the row contains 'Vanguard' to identify fund rows
        if any("Vanguard" in cell for cell in row_data):
            # Find the return date from this row (2nd column)
            return_date_str = row_data[1] if len(row_data) > 1 else ''
            return_date_obj = parse_date(return_date_str)

            # Update the most recent return date if necessary
            if return_date_obj and (most_recent_return_date_obj is None or return_date_obj > most_recent_return_date_obj):
                most_recent_return_date_obj = return_date_obj  # For comparison
                most_recent_return_date_str = return_date_str  # Store as string
            
            # Append the row to the fund_rows list
            fund_rows.append(tuple(row_data))  # Store as tuple to avoid mutable data issues with duplicates

        # Find "Aggregate:" and capture the next row as the portfolio return row
        elif "Aggregate:" in row_data[0]:
            aggregate_found = True
            # Check if there's a next row to capture as the portfolio return row
            if idx + 1 < len(rows):
                next_row_data = rows[idx + 1].xpath('ss:Cell/ss:Data', namespaces=namespaces)
                portfolio_return_row = [clean_text(d.text.strip() if d.text else '') for d in next_row_data]
                
                # Replace `"-"` with the actual portfolio name
                if len(portfolio_return_row) > 0 and portfolio_return_row[0] == "-":
                    portfolio_return_row[0] = portfolio_name
                
                # If there are fewer columns than expected, fill in empty columns
                while len(portfolio_return_row) < len(portfolio_annual_headers):
                    portfolio_return_row.append('')
                portfolio_return_row = tuple(portfolio_return_row)  # Store as tuple to ensure uniformity in duplicates checking

            break  # Stop once we find the "Aggregate:" row and the next row
    
    # Return the fund rows and portfolio return row
    return fund_rows, portfolio_return_row

# Step 6: Process all files in the input directory
all_rows = set()  # Use a set to automatically handle duplicate rows

for filename in os.listdir(input_directory):
    if filename.endswith(".xls"):
        file_path = os.path.join(input_directory, filename)
        print(f"Processing: {file_path}")
        fund_rows, portfolio_return_row = process_file(file_path)

        # Add all fund rows to the set (to ensure no duplicates)
        all_rows.update(fund_rows)

        # Add the portfolio return row (if it exists)
        if portfolio_return_row:
            all_rows.add(portfolio_return_row)

# Step 7: Write the output data to a CSV file
with open(output_file_path, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the headers
    writer.writerow(portfolio_annual_headers)

    # Write all the rows from the set, which now contains no duplicates
    for row in all_rows:
        writer.writerow(row)

# Output completion message
print(f"All files processed and consolidated into: {output_file_path}")
