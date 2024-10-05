import re
import pandas as pd
from bs4 import BeautifulSoup

# File paths
input_file = "/Users/tylermontell/Projects/magic_machine_app/data/trigger_folder/Tracking.htm"
output_file = "/Users/tylermontell/Projects/magic_machine_app/test/output.txt"

# Function to extract and clean relevant content from the HTML
def extract_relevant_content(html_content):
    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract content between the specific classes
    start = soup.find(class_="core-account-notification")
    end = soup.find(class_="sidebar-layout-analytics-controls")
    
    # Extract the relevant section between start and end
    relevant_content = ""
    if start and end:
        for tag in start.find_all_next():
            if tag == end:
                break
            relevant_content += str(tag)

    return relevant_content

# Function to parse relevant fund and portfolio data
def parse_data(cleaned_html):
    soup = BeautifulSoup(cleaned_html, "html.parser")

    data = []

    # Extract both fund and portfolio data
    for section in soup.find_all(class_="allocation-title"):
        # Extract common fields
        short_name = section.find(class_="security-shortname").text.strip() if section.find(class_="security-shortname") else ''
        long_name = section.find(class_="security-longname").text.strip() if section.find(class_="security-longname") else ''
        
        # Extract stats only once per section
        risk_number = section.find_next("img", alt=re.compile("Risk Number"))["src"].split('r')[-1].split('.')[0] if section.find_next("img", alt=re.compile("Risk Number")) else ''
        worst_case = section.find_next("input", class_="worst-case")["placeholder"].replace('%', '').strip() if section.find_next("input", class_="worst-case") else ''
        best_case = section.find_next("input", class_="best-case")["placeholder"].replace('%', '').strip() if section.find_next("input", class_="best-case") else ''
        return_val = section.find_next("input", class_="analysis-return")["placeholder"].replace('%', '').strip() if section.find_next("input", class_="analysis-return") else ''
        stdev = section.find_next("input", class_="stdev")["placeholder"].replace('%', '').strip() if section.find_next("input", class_="stdev") else ''
        dividend = section.find_next("input", class_="ttm-dividend")["placeholder"].replace('%', '').strip() if section.find_next("input", class_="ttm-dividend") else ''
        fee = section.find_next("input", class_="annual-fee")["placeholder"].replace('%', '').strip() if section.find_next("input", class_="annual-fee") else ''
        
        # Append data as a single row
        if short_name or long_name:
            data.append([short_name, long_name, risk_number, worst_case, best_case, return_val, stdev, dividend, fee])

    return data

# Function to write data to a text file as a dataframe
def write_data_to_file(data, output_file):
    # Create DataFrame
    columns = ["ticker", "name", "r_risk_score", "low_6mo_return", "high_6mo_return", "pot_6mo_return", "vol", "est_dividend", "r_net_expense"]

    df = pd.DataFrame(data, columns=columns)

    # Remove any duplicate rows
    df = df.drop_duplicates()

    # Write to file
    with open(output_file, "w") as f:
        f.write(df.to_string(index=False))

# Main script execution
if __name__ == "__main__":
    with open(input_file, "r") as f:
        html_content = f.read()

    # Step 1: Extract relevant content
    cleaned_content = extract_relevant_content(html_content)

    # Step 2: Parse the data (both funds and portfolios)
    parsed_data = parse_data(cleaned_content)

    # Step 3: Write the parsed data to the output file
    write_data_to_file(parsed_data, output_file)

    print(f"Data successfully extracted and written to {output_file}")
