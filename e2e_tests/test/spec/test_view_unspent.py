# pylint: disable=redefined-outer-name, unused-import
"""
Tests for view unspent list.
"""
from __future__ import annotations

import allure
import pytest

from accessible_constant import FIRST_APPLICATION
from accessible_constant import FIRST_APPLICATION_URL
from e2e_tests.test.utilities.app_setup import test_environment
from e2e_tests.test.utilities.app_setup import wallets_and_operations
from e2e_tests.test.utilities.app_setup import WalletTestSetup
from src.model.enums.enums_model import WalletType


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('View Unspent List')
@allure.story('Verify outpoint in unspent list')
def test_view_unspent_list(wallets_and_operations: WalletTestSetup):
    """
    Test view unspent list.
    """

    if wallets_and_operations.wallet_mode == WalletType.EMBEDDED_TYPE_WALLET.value:
        with allure.step('Create embedded wallet'):
            wallets_and_operations.first_page_features.wallet_features.create_embedded_wallet(
                FIRST_APPLICATION,
            )
    else:
        with allure.step('Connect to external wallet'):
            wallets_and_operations.first_page_features.wallet_features.connect_wallet(
                application=FIRST_APPLICATION, url=FIRST_APPLICATION_URL,
            )

    with allure.step('Fund the wallet'):
        wallets_and_operations.first_page_features.wallet_features.fund_wallet(
            FIRST_APPLICATION,
        )

    with allure.step('verifies the outpoint'):
        wallets_and_operations.first_page_objects.sidebar_page_objects.click_view_unspents_button()
        wallets_and_operations.first_page_objects.view_unspent_list_page_objects.click_unspent_frame()
        actual_outpoint = wallets_and_operations.first_page_objects.view_unspent_list_page_objects.get_unspent_utxo_outpoint()
        outpoint = wallets_and_operations.first_page_operations.do_get_copied_address()

        assert actual_outpoint == outpoint
