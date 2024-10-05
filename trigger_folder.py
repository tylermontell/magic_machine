
# trigger_folder.py

import os
import re
import logging
from config import TRIGGER_FOLDER, NAMESPACES

# Set up logging
logger = logging.getLogger(__name__)

def standardize_file_name(file_name):
    """
    Standardize the file name by:
    - Converting to lowercase
    - Replacing spaces with underscores
    - Removing special characters
    """
    # Convert to lowercase
    file_name = file_name.lower()
    
    # Replace spaces with underscores
    file_name = file_name.replace(' ', '_')
    
    # Remove any characters that are not alphanumeric, underscores, or periods (for file extensions)
    file_name = re.sub(r'[^\w\._]', '', file_name)
    
    return file_name

def rename_files_in_trigger_folder():
    """
    Rename files in the trigger_folder to computer-readable, standardized names.
    """
    for file_name in os.listdir(TRIGGER_FOLDER):
        file_path = os.path.join(TRIGGER_FOLDER, file_name)
        
        # Ignore directories, only rename files
        if os.path.isfile(file_path):
            new_file_name = standardize_file_name(file_name)
            new_file_path = os.path.join(TRIGGER_FOLDER, new_file_name)
            
            # Rename the file if the new name is different from the old name
            if new_file_name != file_name:
                try:
                    os.rename(file_path, new_file_path)
                    logger.info(f"Renamed {file_name} to {new_file_name}")
                except Exception as e:
                    logger.error(f"Error renaming file {file_name}: {e}")

# Call this function at the start of your file processing workflow
rename_files_in_trigger_folder()
