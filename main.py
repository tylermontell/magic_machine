# main.py

import argparse
import logging
from parsers.general_parser import process_files  # Corrected import path
from config import LOG_FILE, TRIGGER_FOLDER  # Assuming these paths are defined in config

def configure_logging(log_file):
    """
    Configures logging to log to both a file and the console with reduced verbosity.
    """
    logging.basicConfig(
        level=logging.WARNING,  # Reduce verbosity by only logging WARNING and above
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, mode='w'),  # Logs to a file, overwrites each time
            logging.StreamHandler()  # Logs to the console
        ]
    )

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Mutual Fund Data Parser')
    parser.add_argument('--process', action='store_true', help='Process new files in the trigger folder.')
    args = parser.parse_args()

    # Configure logging
    configure_logging(LOG_FILE)
    logger = logging.getLogger(__name__)

    if args.process:
        logger.info('Starting the file processing.')
        try:
            process_files(TRIGGER_FOLDER)  # Pass the trigger folder to the file processor
            logger.info('File processing completed successfully.')
        except Exception as e:
            logger.error(f'An error occurred: {e}')
    else:
        logger.info('No action specified. Use --process to process new files.')
        parser.print_help()

if __name__ == '__main__':
    main()

