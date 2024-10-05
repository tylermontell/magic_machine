# parsers/xlsx_parser.py

import pandas as pd
import logging
import openpyxl
import os
from config import NAMESPACES

logger = logging.getLogger(__name__)

def save_to_excel(data, filename):
    """
    Save the parsed data to an Excel file.
    """
    # Define the output directory
    output_directory = '/Users/tylermontell/Projects/magic_machine_app/data/output'

    # Ensure the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)  # Create the directory if it doesn't exist

    # Define the full path for the output file
    file_path = os.path.join(output_directory, filename)

    # Save data to an Excel file using pandas
    df = pd.DataFrame(data)  # Assuming 'data' is in a form that can be converted to a DataFrame
    df.to_excel(file_path, index=False)

    # Log the successful save
    logger.info(f"Data saved to {file_path}")

def process_xlsx(file_path):
    """
    Parse and process an .xlsx file, then save to an output directory.
    """
    try:
        # Parse the xlsx file
        data = parse_xlsx_file(file_path)  # Parse and return data
        
        # Define output filename based on the input file
        filename = os.path.basename(file_path).replace('.xlsx', '_output.xlsx')

        # Call the save function to write data to an Excel file
        save_to_excel(data, filename)
        
    except Exception as e:
        logger.error(f"Error processing .xlsx file {file_path}: {e}")

def parse_xlsx_file(file_path):
    """
    Function to parse the .xlsx file and extract data.
    This should return the parsed data in a format that can be saved, like a list of dictionaries.
    """
    try:
        # Load the xlsx file
        data = pd.read_excel(file_path)
        
        # Convert the data to a dictionary or list of dictionaries if needed
        extracted_data = data.to_dict(orient='records')
        
        # Log the successful parsing
        logger.info(f"Parsed {len(extracted_data)} rows from {file_path}")
        
        return extracted_data
    
    except Exception as e:
        logger.error(f"Error parsing .xlsx file {file_path}: {e}")
        return []
