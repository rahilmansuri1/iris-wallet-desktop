# pylint: disable=redefined-outer-name, unused-import
"""
    E2E test for login app authentication
"""
from __future__ import annotations

import os

import allure
import pytest
from dogtail.rawinput import keyCombo
from dogtail.rawinput import typeText
from dotenv import load_dotenv

from accessible_constant import FIRST_APPLICATION
from accessible_constant import FIRST_APPLICATION_URL
from e2e_tests.test.utilities.app_setup import test_environment
from e2e_tests.test.utilities.app_setup import wallets_and_operations
from e2e_tests.test.utilities.app_setup import WalletTestSetup

load_dotenv()
AUTHENTICATION_PASSWORD = os.getenv('AUTHENTICATION_PASSWORD')


@allure.feature('Login App')
@allure.story('Test Login App Toggle Button')
@pytest.mark.parametrize('test_environment', [False], indirect=True)
def test_login_app_toggle_button_on(test_environment, wallets_and_operations: WalletTestSetup):
    """
    Test the login app toggle button functionality.

    This test case creates first wallet,
    toggles the login app auth button to on, and restarts the application.

    Args:
        test_environment: The test environment setup.
        wallets_and_operations: The wallets and operations setup.

    Returns:
        None
    """
    with allure.step('Create and fund first wallet'):
        wallets_and_operations.first_page_features.wallet_features.create_and_fund_wallet(
            wallets_and_operations=wallets_and_operations, application=FIRST_APPLICATION, application_url=FIRST_APPLICATION_URL, fund=False,
        )

    with allure.step('Toggle the login app auth button to on and restart the application'):
        wallets_and_operations.first_page_objects.sidebar_page_objects.click_settings_button()
        wallets_and_operations.first_page_objects.settings_page_objects.click_login_app_toggle_button()

        test_environment.restart(reset_data=False)


@allure.feature('Login App')
@allure.story('Test Login App with Authentication')
@pytest.mark.parametrize('test_environment', [False], indirect=True)
def test_login_app_with_authentication(wallets_and_operations: WalletTestSetup):
    """
    Test the login app with authentication functionality.

    This test case types the login password, asserts the state of the toggle button,
    toggles it to off, and types the login password again.

    Args:
        test_environment: The test environment setup.
        wallets_and_operations: The wallets and operations setup.

    Returns:
        None
    """
    with allure.step('assert the state of toggle button and toggle it to off'):
        typeText(AUTHENTICATION_PASSWORD)
        keyCombo('enter')
        wallets_and_operations.first_page_objects.sidebar_page_objects.click_settings_button()
        assert True is wallets_and_operations.first_page_objects.settings_page_objects.login_auth_toggle_button().checked
        wallets_and_operations.first_page_objects.settings_page_objects.click_login_app_toggle_button()

        typeText(AUTHENTICATION_PASSWORD)
        keyCombo('enter')

        assert False is wallets_and_operations.first_page_objects.settings_page_objects.login_auth_toggle_button().checked
