"""Unit test for logger class"""
# pylint: disable=redefined-outer-name,unused-argument,too-many-arguments
from __future__ import annotations

import logging
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from src.utils.constant import LOG_FILE_MAX_BACKUP_COUNT
from src.utils.constant import LOG_FILE_MAX_SIZE
from src.utils.logging import setup_logging  # Adjust import path as needed


class TestSetupLogging(unittest.TestCase):
    """Unit test for logger class """
    @patch('src.utils.logging.local_store')
    @patch('src.utils.logging.RotatingFileHandler')
    @patch('src.utils.logging.StreamHandler')
    @patch('src.utils.logging.logging.getLogger')
    def test_setup_logging_production(self, mock_get_logger, mock_stream_handler, mock_rotating_file_handler, mock_local_store):
        """Test logging setup in production mode."""
        # Setup mocks
        mock_local_store.create_folder.return_value = 'mock_log_path'
        mock_logger_instance = MagicMock()
        mock_get_logger.return_value = mock_logger_instance
        mock_rotating_file_handler_instance = MagicMock()
        mock_rotating_file_handler.return_value = mock_rotating_file_handler_instance

        setup_logging('production')

        # Check logger configuration
        mock_get_logger.assert_called_once_with('iris-wallet')
        mock_logger_instance.setLevel.assert_called_once_with(logging.DEBUG)
        mock_logger_instance.propagate = False

        # Check file handler setup
        mock_rotating_file_handler.assert_called_once_with(
            'mock_log_path/iris_wallet_desktop.log',
            maxBytes=LOG_FILE_MAX_SIZE,
            backupCount=LOG_FILE_MAX_BACKUP_COUNT,
        )
        mock_rotating_file_handler_instance.setFormatter.assert_called_once()
        mock_rotating_file_handler_instance.setLevel.assert_called_once_with(
            logging.ERROR,
        )

        # Check that only the file handler was added
        mock_logger_instance.addHandler.assert_called_once_with(
            mock_rotating_file_handler_instance,
        )

    @patch('src.utils.logging.local_store')
    @patch('src.utils.logging.RotatingFileHandler')
    @patch('src.utils.logging.StreamHandler')
    @patch('src.utils.logging.logging.getLogger')
    def test_setup_logging_development(self, mock_get_logger, mock_stream_handler, mock_rotating_file_handler, mock_local_store):
        """Test logging setup in development mode."""
        # Setup mocks
        mock_local_store.create_folder.return_value = 'mock_log_path'
        mock_logger_instance = MagicMock()
        mock_get_logger.return_value = mock_logger_instance
        mock_rotating_file_handler_instance = MagicMock()
        mock_rotating_file_handler.return_value = mock_rotating_file_handler_instance
        mock_console_handler_instance = MagicMock()
        mock_stream_handler.return_value = mock_console_handler_instance

        setup_logging('development')

        # Check logger configuration
        mock_get_logger.assert_called_once_with('iris-wallet')
        mock_logger_instance.setLevel.assert_called_once_with(logging.DEBUG)
        mock_logger_instance.propagate = False

        # Check file handler setup
        mock_rotating_file_handler.assert_called_once_with(
            'mock_log_path/iris_wallet_desktop.log',
            maxBytes=LOG_FILE_MAX_SIZE,
            backupCount=LOG_FILE_MAX_BACKUP_COUNT,
        )
        mock_rotating_file_handler_instance.setFormatter.assert_called_once()
        mock_rotating_file_handler_instance.setLevel.assert_called_once_with(
            logging.DEBUG,
        )

        # Check console handler setup
        mock_console_handler_instance.setFormatter.assert_called_once()
        mock_console_handler_instance.setLevel.assert_called_once_with(
            logging.DEBUG,
        )

        # Check handlers are added correctly
        handlers = [
            mock_rotating_file_handler_instance,
            mock_console_handler_instance,
        ]
        mock_logger_instance.addHandler.assert_has_calls(
            [unittest.mock.call(handler) for handler in handlers],
        )
