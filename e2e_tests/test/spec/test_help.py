# pylint: disable=redefined-outer-name, unused-import
"""Test module for help page"""
from __future__ import annotations

import allure
import pytest

from accessible_constant import FIRST_APPLICATION
from accessible_constant import FIRST_APPLICATION_URL
from e2e_tests.test.utilities.app_setup import test_environment
from e2e_tests.test.utilities.app_setup import wallets_and_operations
from e2e_tests.test.utilities.model import WalletTestSetup


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('Help page test')
@allure.story('Tests for elements in Help page')
def test_help_page(wallets_and_operations: WalletTestSetup):
    """Test help page"""
    with allure.step('Initialize the wallet'):
        wallets_and_operations.first_page_features.wallet_features.create_and_fund_wallet(
            wallets_and_operations, FIRST_APPLICATION, FIRST_APPLICATION_URL, fund=False,
        )

    with allure.step('Navigating to help page'):
        wallets_and_operations.first_page_operations.do_focus_on_application(
            FIRST_APPLICATION,
        )
        wallets_and_operations.first_page_objects.sidebar_page_objects.click_help_button()

    with allure.step('clicking the first card'):
        wallets_and_operations.first_page_objects.help_page_objects.click_testnet_bitcoin()
        help_card_1_title = wallets_and_operations.first_page_objects.help_page_objects.get_testnet_bitcoin_frame_title()

        assert help_card_1_title == 'Why can I get TESTNET Bitcoins?'

    with allure.step('clicking the second card'):
        wallets_and_operations.first_page_objects.help_page_objects.click_bitcoin_txn()
        help_card_2_title = wallets_and_operations.first_page_objects.help_page_objects.get_bitcoin_txn_frame_label()

        assert help_card_2_title == 'Why do I see outgoing Bitcoin transactions that I didn\'t authorize?'
