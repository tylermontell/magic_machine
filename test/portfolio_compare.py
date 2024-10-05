import os
from lxml import etree
import csv
import pandas as pd
from datetime import datetime
from config import portfolio_compare_headers  # Importing the portfolio headers from the config file

# Define the directories
input_directory = '/Users/tylermontell/Projects/Magic_Machine/mstar_portfolio/Test'
output_file_path = '/Users/tylermontell/Projects/Magic_Machine/mstar_portfolio/Outputs/consolidated_portfolio_data.csv'

# Create output directory if it doesn't exist
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# Define XML namespaces
namespaces = {
    'ss': 'urn:schemas-microsoft-com:office:spreadsheet'
}

# Helper function to parse date strings
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None

# List to hold all the rows across all files
all_data_rows = []

# Function to process each file
def process_file(input_file_path):
    print(f"Processing: {input_file_path}")
    
    with open(input_file_path, 'rb') as file:
        xml_data = file.read()

    # Parse the XML file
    root = etree.fromstring(xml_data)

    # Initialize variables to capture key information
    portfolio_name = None  # Set to None initially
    fund_rows = []
    portfolio_return_row = None
    most_recent_return_date_str = None
    most_recent_return_date_obj = None

    # Step 1: Detect the portfolio name (Meridian or G Portfolio)
    for data in root.xpath('//ss:Data', namespaces=namespaces):
        text_content = data.text.strip() if data.text else ''
        if text_content.startswith("Meridian") or text_content.startswith("G "):
            portfolio_name = text_content
            break

    # Step 2: If no valid portfolio name is found, skip processing
    if not portfolio_name:
        print(f"Skipping file {input_file_path} due to missing portfolio name.")
        return  # Exit the function without adding any data for this file

    # Step 3: Extract fund rows and locate the "Aggregate:" row
    rows = root.xpath('//ss:Row', namespaces=namespaces)
    aggregate_found = False

    for idx, data in enumerate(rows):
        row_data = [d.text.strip() if d.text else '' for d in data.xpath('ss:Cell/ss:Data', namespaces=namespaces)]
        
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
            fund_rows.append(row_data)

        # Step 4: Find "Aggregate:" and capture the next row as the portfolio return row
        elif "Aggregate:" in row_data[0]:
            aggregate_found = True
            # Check if there's a next row to capture as the portfolio return row
            if idx + 1 < len(rows):
                next_row_data = rows[idx + 1].xpath('ss:Cell/ss:Data', namespaces=namespaces)
                portfolio_return_row = [d.text.strip() if d.text else '' for d in next_row_data]
            break  # Stop once we find the "Aggregate:" row and the next row

    # Step 5: Add the portfolio name and most recent return date to the portfolio return row
    if portfolio_return_row:
        # Ensure the portfolio_return_row has at least 2 columns
        if len(portfolio_return_row) < 2:
            portfolio_return_row.extend([''] * (2 - len(portfolio_return_row)))
        
        # Update the first two columns with the portfolio name and return date
        portfolio_return_row[0] = portfolio_name
        portfolio_return_row[1] = most_recent_return_date_str if most_recent_return_date_str else "N/A"
    else:
        # Fallback in case "Aggregate:" row wasn't found, create an empty row
        portfolio_return_row = [portfolio_name, most_recent_return_date_str if most_recent_return_date_str else "N/A"] + \
                               [""] * (len(portfolio_headers) - 2)

    # Step 6: Append all fund rows and portfolio return row to the combined list
    all_data_rows.extend(fund_rows)  # Add all component fund rows
    all_data_rows.append(portfolio_return_row)  # Add the portfolio return row

# Step 7: Iterate through all files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".xls"):
        input_file = os.path.join(input_directory, filename)
        process_file(input_file)

# Step 8: Remove duplicates from the combined data
# Convert to a DataFrame for easier duplicate removal
df = pd.DataFrame(all_data_rows, columns=portfolio_compare_headers)

# Drop duplicate rows based on 'Name' and 'Return Date (current)' columns
df.drop_duplicates(subset=['Name', 'Return Date (current)'], keep='first', inplace=True)

# Step 9: Write the final DataFrame to a single consolidated CSV file
df.to_csv(output_file_path, index=False)

print(f"All files processed and consolidated into: {output_file_path}")
