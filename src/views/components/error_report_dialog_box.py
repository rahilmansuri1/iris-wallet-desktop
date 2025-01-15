"""
This module defines the ErrorReportDialog class, which represents a message box
for sending error reports with translations and error details.
"""
from __future__ import annotations

import shutil

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QMessageBox

from config import report_email_server_config
from src.utils.common_utils import generate_error_report_email
from src.utils.common_utils import send_crash_report_async
from src.utils.common_utils import zip_logger_folder
from src.utils.error_message import ERROR_OPERATION_CANCELLED
from src.utils.info_message import INFO_SENDING_ERROR_REPORT
from src.utils.local_store import local_store
from src.version import __version__
from src.views.components.toast import ToastManager


class ErrorReportDialog(QMessageBox):
    """This class represents the error report dialog in the application."""

    def __init__(self, url, parent=None):
        """Initialize the ErrorReportDialog message box with translated strings and error details."""
        super().__init__(parent)
        self.url = url
        self.setWindowTitle('Send Error Report')
        # Create the message box
        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle(
            QCoreApplication.translate(
                'iris_wallet_desktop', 'error_report', None,
            ),
        )

        # Fetch translations
        self.text_sorry = QCoreApplication.translate(
            'iris_wallet_desktop', 'something_went_wrong_mb', None,
        )
        self.text_help = QCoreApplication.translate(
            'iris_wallet_desktop', 'error_description_mb', None,
        )
        self.text_included = QCoreApplication.translate(
            'iris_wallet_desktop', 'what_will_be_included', None,
        )
        self.text_error_details = QCoreApplication.translate(
            'iris_wallet_desktop', 'error_details_title', None,
        )
        self.text_app_version = QCoreApplication.translate(
            'iris_wallet_desktop', 'application_version', None,
        )
        self.text_os_info = QCoreApplication.translate(
            'iris_wallet_desktop', 'os_info', None,
        )
        self.text_send_report = QCoreApplication.translate(
            'iris_wallet_desktop', 'error_report_permission', None,
        )

        # Set the text for the message box
        self.setText(self.text_sorry)
        self.setInformativeText(
            f"{self.text_help}\n\n"
            f"{self.text_included}\n"
            f"{self.text_error_details}\n"
            f"{self.text_app_version}\n"
            f"{self.text_os_info}\n\n"
            f"{self.text_send_report}",
        )
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.Yes)

        # Connect the buttonClicked signal to a custom slot
        self.buttonClicked.connect(self.on_button_clicked)

    def on_button_clicked(self, button):
        """
        Handles the button click event to either send an error report or cancel the operation.

        If the 'Yes' button is clicked:
        - Shows an info toast notification indicating the report is being sent.
        - Compresses the log files into a ZIP archive.
        - Prepares an error report email with the appropriate subject and body.
        - Sends the error report asynchronously to the specified email ID.

        If the 'No' button is clicked:
        - Shows a warning toast notification indicating the operation was cancelled.
        """
        if button == self.button(QMessageBox.Yes):
            ToastManager.info(INFO_SENDING_ERROR_REPORT)

            base_path = local_store.get_path()
            _, output_dir = zip_logger_folder(base_path)
            zip_file_path = shutil.make_archive(output_dir, 'zip', output_dir)

            # Set the subject and formatted body
            subject = f"Iris Wallet Error Report - Version {__version__}"
            title = 'Error Report for Iris Wallet Desktop'
            body = generate_error_report_email(url=self.url, title=title)
            email_id = report_email_server_config['email_id']

            send_crash_report_async(email_id, subject, body, zip_file_path)
        elif button == self.button(QMessageBox.No):
            ToastManager.warning(ERROR_OPERATION_CANCELLED)
