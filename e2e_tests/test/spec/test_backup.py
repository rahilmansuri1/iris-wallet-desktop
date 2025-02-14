# pylint: disable=redefined-outer-name, unused-import
"""Test module for the backup page functionality"""
from __future__ import annotations

import os

import allure
import pytest
from dogtail.rawinput import keyCombo
from dotenv import load_dotenv

from accessible_constant import FIRST_APPLICATION
from accessible_constant import FIRST_APPLICATION_URL
from e2e_tests.test.utilities.app_setup import test_environment
from e2e_tests.test.utilities.app_setup import wallets_and_operations
from e2e_tests.test.utilities.app_setup import WalletTestSetup
from src.model.enums.enums_model import WalletType

load_dotenv()
EMAIL_ID = os.getenv('EMAIL_ID')
PASSWORD = os.getenv('PASSWORD')


@pytest.mark.parametrize('test_environment', [False], indirect=True)
def test_backup(wallets_and_operations: WalletTestSetup):
    """Test the backup page functionality"""

    wallets_and_operations.first_page_features.wallet_features.create_embedded_wallet(
        FIRST_APPLICATION,
    )
    wallets_and_operations.first_page_objects.sidebar_page_objects.click_backup_button()
    wallets_and_operations.first_page_objects.backup_page_objects.click_configurable_button()
    wallets_and_operations.first_page_objects.backup_page_objects.click_backup_window()
    wallets_and_operations.first_page_objects.backup_page_objects.enter_email(
        EMAIL_ID,
    )
    wallets_and_operations.first_page_objects.backup_page_objects.click_next_button()
    wallets_and_operations.first_page_objects.backup_page_objects.enter_password(
        PASSWORD,
    )
    wallets_and_operations.first_page_objects.backup_page_objects.click_next_button()
    wallets_and_operations.first_page_objects.backup_page_objects.click_try_another_way_button()
    wallets_and_operations.first_page_objects.backup_page_objects.click_google_authenticator_button()
    code = wallets_and_operations.first_page_objects.backup_page_objects.get_security_otp()
    wallets_and_operations.first_page_objects.backup_page_objects.enter_security_code(
        code,
    )
    wallets_and_operations.first_page_objects.backup_page_objects.click_next_button()
    keyCombo('enter')
    wallets_and_operations.first_page_objects.backup_page_objects.click_continue_button()
