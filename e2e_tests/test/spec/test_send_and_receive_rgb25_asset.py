# pylint: disable=redefined-outer-name, unused-import
"""Iris Wallet Send and Receive Operation Automation Test Suite for rgb25 asset"""
from __future__ import annotations

import allure

from accessible_constant import FIRST_APPLICATION
from accessible_constant import SECOND_APPLICATION
from e2e_tests.test.utilities.app_setup import test_environment
from e2e_tests.test.utilities.app_setup import wallets_and_operations
from src.model.enums.enums_model import TransactionStatusEnumModel

ASSET_NAME = 'RGB25'
ASSET_DESCRIPTION = 'This is rgb25 asset'
ASSET_AMOUNT = '2000'
SEND_AMOUNT = '50'
INVOICE = 'rgb:~/~/utxob:2msKeFq-uPjwpYxVY-jKS2ymYBq-SqmyP3ovg-AGvth8491-J7seMBm?expiry=1709616110&endpoints=rpc://10.0.2.2:3000/json-rpc'
RGB25_TOASTER_DESCRIPTION = 'An unexpected error occurred: The invoice entered is invalid'


@allure.feature('Automation of Send Operation for RGB25 Asset in Iris Wallet')
@allure.story('Testing Send RGB25 Asset with Expired Invoice')
def test_send_rgb25_with_expired_invoice(wallets_and_operations):
    """Test send rgb25 asset with expired invoice"""
    first_page_features, second_page_features, first_page_objects, _, first_page_operations, _ = wallets_and_operations

    with allure.step('Create Embedded Wallet and Fund First Wallet'):
        first_page_features.wallet_features.create_embedded_wallet(
            FIRST_APPLICATION,
        )
        first_page_features.wallet_features.fund_wallet(FIRST_APPLICATION)

    with allure.step('Create Embedded Wallets and Fund Second Wallet'):
        second_page_features.wallet_features.create_embedded_wallet(
            SECOND_APPLICATION,
        )
        second_page_features.wallet_features.fund_wallet(SECOND_APPLICATION)

    with allure.step('Issue RGB25 Asset'):
        first_page_features.issue_rgb25_features.issue_rgb25_with_sufficient_sats_and_utxo(
            application=FIRST_APPLICATION, asset_description=ASSET_DESCRIPTION, asset_name=ASSET_NAME, asset_amount=ASSET_AMOUNT,
        )

    with allure.step('Send RGB25 Asset with Expired Invoice'):
        first_page_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.sidebar_page_objects.click_collectibles_button()
        first_page_objects.collectible_page_objects.click_rgb25_frame(
            ASSET_NAME,
        )
        first_page_objects.asset_detail_page_objects.click_send_button()
        description = first_page_features.send_features.send_with_wrong_invoice(
            application=FIRST_APPLICATION, receiver_invoice=INVOICE, amount=SEND_AMOUNT,
        )

    with allure.step('Verify Error Message'):
        assert description == RGB25_TOASTER_DESCRIPTION


@allure.feature('Automation of Receive, Send, and Transaction Status for RGB25 Asset in Iris Wallet')
@allure.story('End-to-End Testing of Receiving, Sending, and Verifying Transaction Status for RGB25 Asset')
def test_send_and_receive_rgb25_asset_operation(wallets_and_operations):
    """Test send and receive operation for rgb25 asset"""

    first_page_features, second_page_features, first_page_objects, second_page_objects, first_operations, second_operations = wallets_and_operations

    with allure.step('Generate Invoice'):
        invoice = second_page_features.receive_features.receive_asset_from_sidebar(
            SECOND_APPLICATION,
        )

    with allure.step('Send RGB25 Asset'):
        first_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.collectible_page_objects.click_rgb25_frame(
            ASSET_NAME,
        )
        first_page_objects.asset_detail_page_objects.click_send_button()
        first_page_features.send_features.send(
            application=FIRST_APPLICATION, receiver_invoice=invoice, amount=SEND_AMOUNT,
        )

    with allure.step('Verify Transfer Status'):
        first_page_objects.collectible_page_objects.click_rgb25_frame(
            ASSET_NAME,
        )
        actual_transfer_status = first_page_objects.asset_detail_page_objects.get_transfer_status()
        first_page_objects.asset_detail_page_objects.click_close_button()
        first_page_objects.sidebar_page_objects.click_fungibles_button()

    with allure.step('Verify Received Amount'):
        second_operations.do_focus_on_application(SECOND_APPLICATION)
        second_page_objects.sidebar_page_objects.click_collectibles_button()
        second_page_objects.collectible_page_objects.click_refresh_button()
        second_page_objects.collectible_page_objects.click_rgb25_frame(
            ASSET_NAME,
        )
        received_amount = second_page_objects.asset_detail_page_objects.get_on_chain_total_balance()
        second_page_objects.asset_detail_page_objects.click_close_button()
        second_page_objects.sidebar_page_objects.click_fungibles_button()

    with allure.step('Verify Assertions'):
        assert received_amount == SEND_AMOUNT
        assert actual_transfer_status == TransactionStatusEnumModel.WAITING_COUNTERPARTY.value
