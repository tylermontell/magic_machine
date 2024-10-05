# utils.py

import logging
import sys
import pandas as pd
from config import EXCLUDED_CHARACTERS, EXCLUDED_TERMS, NAMESPACES

# Define logger for utils.py
logger = logging.getLogger(__name__)

def clean_data(data):
    """
    Clean the data by removing rows that contain any of the excluded terms
    or characters and ensuring that no excluded characters are present.
    """
    cleaned_data = []

    for row in data:
        # Ensure that any None values are handled safely
        cleaned_row = [cell if cell is not None else '' for cell in row]

        # Remove excluded characters from each cell
        for char in EXCLUDED_CHARACTERS:
            cleaned_row = [cell.replace(char, '') for cell in cleaned_row]

        # Only keep rows where no cell contains any excluded terms
        if not any(term in cell for term in EXCLUDED_TERMS for cell in cleaned_row):
            # Keep rows that have at least one non-excluded value
            if any(cell.strip() not in ['', '-'] for cell in cleaned_row):
                cleaned_data.append(cleaned_row)

    return cleaned_data

def map_headers(data, header_mappings):
    if not data:
        return []
    # Map headers
    original_headers = data[0]
    mapped_headers = [header_mappings.get(header, header) for header in original_headers]
    # Replace headers with mapped headers
    data[0] = mapped_headers
    # Convert list of lists to list of dictionaries
    data_dicts = []
    for row in data[1:]:
        row_dict = dict(zip(mapped_headers, row))
        data_dicts.append(row_dict)
    return data_dicts

def write_sample_output(data, sample_file):
    """
    Write the parsed data to a text file for manual review and display as a DataFrame.
    """
    try:
        if not data:
            logger.warning(f'No data to write for {sample_file}')
            return

        # Convert the parsed data (list of dictionaries) into a DataFrame
        df = pd.DataFrame(data)

        # Save the DataFrame to a .txt file
        df.to_csv(sample_file, sep='\t', index=False)

        # Display the DataFrame to the user
        print(df)

        logger.info(f'Sample output written to {sample_file}')
    
    except Exception as e:
        logger.error(f'Error writing sample output: {e}')

def confirm_and_proceed():
    user_input = input('Review the sample data. Proceed with database insertion? (y/n): ')
    if user_input.lower() != 'y':
        logger.info('Operation cancelled by user.')
        sys.exit()

def setup_logging(log_file_path):
    logging.basicConfig(
        filename=log_file_path,
        filemode='a',  # Append to log file
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
