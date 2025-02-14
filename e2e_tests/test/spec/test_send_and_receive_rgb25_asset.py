# pylint: disable=redefined-outer-name, unused-import
"""Iris Wallet Send and Receive Operation Automation Test Suite for rgb25 asset"""
from __future__ import annotations

import allure

from accessible_constant import FIRST_APPLICATION
from accessible_constant import FIRST_APPLICATION_URL
from accessible_constant import SECOND_APPLICATION
from accessible_constant import SECOND_APPLICATION_URL
from e2e_tests.test.utilities.app_setup import test_environment
from e2e_tests.test.utilities.app_setup import wallets_and_operations
from e2e_tests.test.utilities.app_setup import WalletTestSetup
from src.model.enums.enums_model import TransactionStatusEnumModel

ASSET_NAME = 'RGB25'
ASSET_DESCRIPTION = 'This is rgb25 asset'
ASSET_AMOUNT = '2000'
SEND_AMOUNT = '50'
INVOICE = 'rgb:~/~/utxob:2msKeFq-uPjwpYxVY-jKS2ymYBq-SqmyP3ovg-AGvth8491-J7seMBm?expiry=1709616110&endpoints=rpc://10.0.2.2:3000/json-rpc'
RGB25_TOASTER_DESCRIPTION = 'An unexpected error occurred: The invoice entered is invalid'


@allure.feature('Automation of Send Operation for RGB25 Asset in Iris Wallet')
@allure.story('Testing Send RGB25 Asset with Expired Invoice')
def test_send_rgb25_with_expired_invoice(wallets_and_operations: WalletTestSetup):
    """Test send rgb25 asset with expired invoice"""

    with allure.step('Create and fund first wallet for send and receive rgb25'):
        wallets_and_operations.first_page_features.wallet_features.create_and_fund_wallet(
            wallets_and_operations=wallets_and_operations, application=FIRST_APPLICATION, application_url=FIRST_APPLICATION_URL,
        )

    with allure.step('Create and fund second wallet for send and receive rgb25'):
        wallets_and_operations.second_page_features.wallet_features.create_and_fund_wallet(
            wallets_and_operations=wallets_and_operations, application=SECOND_APPLICATION, application_url=SECOND_APPLICATION_URL,
        )

    with allure.step('Issue RGB25 Asset'):
        wallets_and_operations.first_page_features.issue_rgb25_features.issue_rgb25_with_sufficient_sats_and_utxo(
            application=FIRST_APPLICATION, asset_description=ASSET_DESCRIPTION, asset_name=ASSET_NAME, asset_amount=ASSET_AMOUNT,
        )

    with allure.step('Send RGB25 Asset with Expired Invoice'):
        wallets_and_operations.first_page_operations.do_focus_on_application(
            FIRST_APPLICATION,
        )
        wallets_and_operations.first_page_objects.sidebar_page_objects.click_collectibles_button()
        wallets_and_operations.first_page_objects.collectible_page_objects.click_rgb25_frame(
            ASSET_NAME,
        )
        wallets_and_operations.first_page_objects.asset_detail_page_objects.click_send_button()
        description = wallets_and_operations.first_page_features.send_features.send_with_wrong_invoice(
            application=FIRST_APPLICATION, receiver_invoice=INVOICE, amount=SEND_AMOUNT,
        )

    with allure.step('Verify Error Message'):
        assert description == RGB25_TOASTER_DESCRIPTION


@allure.feature('Automation of Receive, Send, and Transaction Status for RGB25 Asset in Iris Wallet')
@allure.story('End-to-End Testing of Receiving, Sending, and Verifying Transaction Status for RGB25 Asset')
def test_send_and_receive_rgb25_asset_operation(wallets_and_operations: WalletTestSetup):
    """Test send and receive operation for rgb25 asset"""

    with allure.step('Generate Invoice'):
        invoice = wallets_and_operations.second_page_features.receive_features.receive_asset_from_sidebar(
            SECOND_APPLICATION,
        )

    with allure.step('Send RGB25 Asset'):
        wallets_and_operations.first_page_operations.do_focus_on_application(
            FIRST_APPLICATION,
        )
        wallets_and_operations.first_page_objects.collectible_page_objects.click_rgb25_frame(
            ASSET_NAME,
        )
        wallets_and_operations.first_page_objects.asset_detail_page_objects.click_send_button()
        wallets_and_operations.first_page_features.send_features.send(
            application=FIRST_APPLICATION, receiver_invoice=invoice, amount=SEND_AMOUNT,
        )

    with allure.step('Verify Transfer Status'):
        wallets_and_operations.first_page_objects.collectible_page_objects.click_rgb25_frame(
            ASSET_NAME,
        )
        actual_transfer_status = wallets_and_operations.first_page_objects.asset_detail_page_objects.get_transfer_status()
        wallets_and_operations.first_page_objects.asset_detail_page_objects.click_close_button()
        wallets_and_operations.first_page_objects.sidebar_page_objects.click_fungibles_button()

    with allure.step('Verify Received Amount'):
        wallets_and_operations.second_page_operations.do_focus_on_application(
            SECOND_APPLICATION,
        )
        wallets_and_operations.second_page_objects.sidebar_page_objects.click_collectibles_button()
        wallets_and_operations.second_page_objects.collectible_page_objects.click_refresh_button()
        wallets_and_operations.second_page_objects.collectible_page_objects.click_rgb25_frame(
            ASSET_NAME,
        )
        received_amount = wallets_and_operations.second_page_objects.asset_detail_page_objects.get_on_chain_total_balance()
        wallets_and_operations.second_page_objects.asset_detail_page_objects.click_close_button()
        wallets_and_operations.second_page_objects.sidebar_page_objects.click_fungibles_button()

    with allure.step('Verify Assertions'):
        assert received_amount == SEND_AMOUNT
        assert actual_transfer_status == TransactionStatusEnumModel.WAITING_COUNTERPARTY.value
