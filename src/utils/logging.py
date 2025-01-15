"""Sets up the logging configuration for the application."""
from __future__ import annotations

import logging
import os
import sys
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

from src.utils.constant import LOG_FILE_MAX_BACKUP_COUNT
from src.utils.constant import LOG_FILE_MAX_SIZE
from src.utils.constant import LOG_FOLDER_NAME
from src.utils.local_store import local_store


def setup_logging(application_status: str) -> logging.Logger:
    """
    Sets up the logging configuration for the application.

    Depending on the application status (production or development), it configures
    different logging handlers. For production, it logs to a file with a defined
    size limit and backup count. For development, it logs both to a file and the console.

    Args:
        application_status (str): The current status of the application, either 'production' or 'development'.

    Returns:
        logging.Logger: Configured logger instance for the application.
    """
    log_directory = LOG_FOLDER_NAME
    path = local_store.create_folder(log_directory)

    # Create a logger
    logger_instance = logging.getLogger('iris-wallet')
    # Set to debug to capture all levels of messages
    logger_instance.setLevel(logging.DEBUG)
    # Prevent logging from propagating to the root logger
    logger_instance.propagate = False

    # Define formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    file_name = os.path.join(path, 'iris_wallet_desktop.log')

    # Define and add handlers based on network
    file_handler = RotatingFileHandler(
        file_name,
        maxBytes=LOG_FILE_MAX_SIZE,
        backupCount=LOG_FILE_MAX_BACKUP_COUNT,
    )
    file_handler.setFormatter(formatter)
    logger_instance.addHandler(file_handler)

    if application_status == 'production':
        file_handler.setLevel(logging.ERROR)  # Capture info and error messages
    else:
        # Capture debug, info, warnings, and errors
        file_handler.setLevel(logging.DEBUG)

        console_handler = StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.DEBUG)
        logger_instance.addHandler(console_handler)

    return logger_instance


# Determine the application status based on the execution environment
APPLICATION_STATUS = 'production' if getattr(
    sys, 'frozen', False,
) else 'development'

# Set up logging based on the current network
logger = setup_logging(APPLICATION_STATUS)
