"""Unit test for error report dialog component."""
# Disable the redefined-outer-name warning as
# it's normal to pass mocked objects in test functions
# pylint: disable=redefined-outer-name,unused-argument,protected-access
from __future__ import annotations

from unittest.mock import patch

import pytest
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QMessageBox

from src.utils.error_message import ERROR_OPERATION_CANCELLED
from src.utils.info_message import INFO_SENDING_ERROR_REPORT
from src.utils.local_store import local_store
from src.version import __version__
from src.views.components.error_report_dialog_box import ErrorReportDialog


@pytest.fixture
def error_report_dialog(qtbot):
    """Fixture to create and return an instance of ErrorReportDialog."""
    url = 'http://example.com/error_report'
    dialog = ErrorReportDialog(url)
    return dialog


def test_dialog_initialization(error_report_dialog):
    """Test if the ErrorReportDialog initializes with correct properties."""
    dialog = error_report_dialog

    expected_title = QCoreApplication.translate(
        'iris_wallet_desktop', 'error_report', None,
    )
    assert dialog.windowTitle() == expected_title
    # Test the text in the dialog
    assert 'something_went_wrong_mb' in dialog.text_sorry
    assert 'error_description_mb' in dialog.text_help
    assert 'what_will_be_included' in dialog.text_included

    # Verify the dialog has 'Yes' and 'No' buttons
    buttons = dialog.buttons()
    assert len(buttons) == 2
    assert buttons[0].text().replace('&', '') == 'Yes'
    assert buttons[1].text().replace('&', '') == 'No'


def test_send_report_on_yes_button(error_report_dialog):
    """Test behavior when the 'Yes' button is clicked."""
    dialog = error_report_dialog

    # Mock external functions to prevent actual side effects during testing
    with patch('src.views.components.error_report_dialog_box.ToastManager.info') as mock_info, \
            patch('src.views.components.error_report_dialog_box.zip_logger_folder') as mock_zip, \
            patch('src.views.components.error_report_dialog_box.shutil.make_archive') as mock_archive, \
            patch('src.views.components.error_report_dialog_box.generate_error_report_email') as mock_generate_email, \
            patch('src.views.components.error_report_dialog_box.send_crash_report_async') as mock_send_email, \
            patch('src.views.components.error_report_dialog_box.report_email_server_config', {'email_id': 'dummy_email_id'}):  # Mock email config dictionary

        # Mock return values for external functions
        mock_zip.return_value = ('dummy_dir', 'output_dir')
        mock_archive.return_value = 'dummy_path.zip'
        mock_generate_email.return_value = 'dummy email body'

        # Simulate a button click on "Yes"
        dialog.buttonClicked.emit(dialog.button(QMessageBox.Yes))

        # Verify that the correct toast message is shown
        mock_info.assert_called_once_with(INFO_SENDING_ERROR_REPORT)

        # Verify that the zip logger folder was called
        mock_zip.assert_called_once_with(local_store.get_path())

        # Verify that make_archive was called to create the ZIP file
        # Corrected the argument order to match the actual function call
        mock_archive.assert_called_once_with('output_dir', 'zip', 'output_dir')

        # Verify the email generation
        mock_generate_email.assert_called_once_with(
            url='http://example.com/error_report', title='Error Report for Iris Wallet Desktop',
        )

        # Verify that the email sending function was called with correct parameters
        mock_send_email.assert_called_once_with(
            'dummy_email_id',  # The mocked email ID
            f"Iris Wallet Error Report - Version {__version__}",
            'dummy email body',
            'dummy_path.zip',
        )


def test_cancel_report_on_no_button(error_report_dialog):
    """Test behavior when the 'No' button is clicked."""
    dialog = error_report_dialog

    # Mock ToastManager to avoid actual toast notifications
    with patch('src.views.components.error_report_dialog_box.ToastManager.warning') as mock_warning:
        # Simulate a button click on "No"
        dialog.buttonClicked.emit(dialog.button(QMessageBox.No))

        # Verify the correct warning toast message is shown
        mock_warning.assert_called_once_with(ERROR_OPERATION_CANCELLED)


def test_dialog_buttons_functionality(error_report_dialog):
    """Test if the 'Yes' and 'No' buttons work correctly."""
    dialog = error_report_dialog

    # Mock ToastManager methods to prevent actual toasts from being shown
    with patch('src.views.components.error_report_dialog_box.ToastManager.info') as mock_info, \
            patch('src.views.components.error_report_dialog_box.ToastManager.warning') as mock_warning:

        # Check 'Yes' button functionality
        yes_button = dialog.button(QMessageBox.Yes)
        assert yes_button.text().replace('&', '') == 'Yes'
        dialog.buttonClicked.emit(yes_button)

        # Verify that the info toast was shown
        mock_info.assert_called_once_with(INFO_SENDING_ERROR_REPORT)

        # Check 'No' button functionality
        no_button = dialog.button(QMessageBox.No)
        assert no_button.text().replace('&', '') == 'No'
        dialog.buttonClicked.emit(no_button)

        # Verify that the warning toast was shown
        mock_warning.assert_called_once_with(ERROR_OPERATION_CANCELLED)
