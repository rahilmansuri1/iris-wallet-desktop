# pylint: disable=redefined-outer-name, unused-import
"""Iris Wallet Send and Receive Operation Automation Test Suite for Bitcoin.
Test suite for Iris Wallet's send and receive operations with Bitcoin."""
from __future__ import annotations

import re

import allure

from accessible_constant import FIRST_APPLICATION
from accessible_constant import FIRST_APPLICATION_URL
from accessible_constant import SECOND_APPLICATION
from accessible_constant import SECOND_APPLICATION_URL
from e2e_tests.test.utilities.app_setup import test_environment
from e2e_tests.test.utilities.app_setup import wallets_and_operations
from e2e_tests.test.utilities.app_setup import WalletTestSetup
from e2e_tests.test.utilities.model import TransferType
from src.model.enums.enums_model import WalletType

AMOUNT = '50000000'
AVAILABLE_BALANCE = '49999347'
AMOUNT_VALIDATION = 'The payment amount exceeds the spendable balance'
SEND_BITCOIN_TOASTER_DESCRIPTION = 'The address is invalid'
FEE_RATE = '8'


@allure.feature('Iris Wallet Send operation with zero balance')
@allure.story('Wallet send operation with zero balance which will give error label')
def test_send_bitcoin_with_zero_balance(wallets_and_operations: WalletTestSetup):
    """Test sending bitcoin with zero balance."""

    with allure.step('Create and fund first wallet for send and receive bitcoin'):
        wallets_and_operations.first_page_features.wallet_features.create_and_fund_wallet(
            wallets_and_operations=wallets_and_operations, application=FIRST_APPLICATION, application_url=FIRST_APPLICATION_URL, fund=False,
        )

    with allure.step('Get bitcoin address'):
        wallets_and_operations.first_page_objects.fungible_page_objects.click_bitcoin_frame()
        wallets_and_operations.first_page_objects.bitcoin_detail_page_objects.click_receive_bitcoin_button()
        address, copied_address = wallets_and_operations.first_page_features.receive_features.receive(
            application=FIRST_APPLICATION, transfer_type=TransferType.BITCOIN.value,
        )

    with allure.step('Verify address'):
        assert copied_address == address

    with allure.step('Send bitcoin with zero balance'):
        wallets_and_operations.first_page_objects.bitcoin_detail_page_objects.click_send_bitcoin_button()
        validation = wallets_and_operations.first_page_features.send_features.send_with_no_fund(
            application=FIRST_APPLICATION, receiver_invoice=copied_address, amount=AMOUNT, transfer_type=TransferType.BITCOIN.value,
        )

    with allure.step('Verify error message'):
        assert validation == AMOUNT_VALIDATION

    with allure.step('Close bitcoin detail page'):
        wallets_and_operations.first_page_objects.bitcoin_detail_page_objects.click_bitcoin_close_button()


@allure.feature('Iris Wallet Receive and Send Operation Automation for bitcoin')
@allure.story('Wallet Receive and Send Operation Automation for bitcoin')
def test_receive_and_send_bitcoin(wallets_and_operations: WalletTestSetup):
    """Test receiving and sending bitcoin."""

    with allure.step('Fund First wallet'):
        wallets_and_operations.first_page_features.wallet_features.fund_wallet(
            FIRST_APPLICATION,
        )

    if wallets_and_operations.wallet_mode == WalletType.EMBEDDED_TYPE_WALLET.value:
        with allure.step('Create Second embedded wallet'):
            wallets_and_operations.second_page_features.wallet_features.create_embedded_wallet(
                SECOND_APPLICATION,
            )
    else:
        with allure.step('Connect to Second external wallet'):
            wallets_and_operations.second_page_features.wallet_features.connect_wallet(
                application=SECOND_APPLICATION, url=SECOND_APPLICATION_URL,
            )

    with allure.step('Get bitcoin address'):
        wallets_and_operations.second_page_operations.do_focus_on_application(
            SECOND_APPLICATION,
        )
        wallets_and_operations.second_page_objects.fungible_page_objects.click_bitcoin_frame()
        wallets_and_operations.second_page_objects.bitcoin_detail_page_objects.click_receive_bitcoin_button()
        address, copied_address = wallets_and_operations.second_page_features.receive_features.receive(
            application=SECOND_APPLICATION, transfer_type=TransferType.BITCOIN.value,
        )

    with allure.step('Verify address'):
        assert copied_address == address

    with allure.step('Send bitcoin'):
        wallets_and_operations.first_page_operations.do_focus_on_application(
            FIRST_APPLICATION,
        )
        wallets_and_operations.first_page_objects.fungible_page_objects.click_bitcoin_frame()
        wallets_and_operations.first_page_objects.bitcoin_detail_page_objects.click_send_bitcoin_button()
        wallets_and_operations.first_page_features.send_features.send(
            application=FIRST_APPLICATION, receiver_invoice=copied_address, amount=AMOUNT, transfer_type=TransferType.BITCOIN.value,
        )

    with allure.step('Refresh bitcoin page'):
        wallets_and_operations.second_page_operations.do_focus_on_application(
            SECOND_APPLICATION,
        )
        wallets_and_operations.second_page_objects.bitcoin_detail_page_objects.click_bitcoin_refresh_button()

    with allure.step('Verify received balance'):
        received_balance = wallets_and_operations.second_page_objects.bitcoin_detail_page_objects.get_total_balance()
        received_balance = received_balance.replace(' SATS', '')
        assert received_balance == AMOUNT

    with allure.step('Close bitcoin detail page'):
        wallets_and_operations.second_page_objects.bitcoin_detail_page_objects.click_bitcoin_close_button()

    with allure.step('Verify balance in first application'):
        wallets_and_operations.first_page_operations.do_focus_on_application(
            FIRST_APPLICATION,
        )
        available_balance = wallets_and_operations.first_page_objects.bitcoin_detail_page_objects.get_total_balance()
        available_balance = available_balance.replace(' SATS', '')
        assert available_balance == AVAILABLE_BALANCE

    with allure.step('Close bitcoin detail page in first application'):
        wallets_and_operations.first_page_objects.bitcoin_detail_page_objects.click_bitcoin_close_button()


@allure.feature('Iris Wallet Send Operation with Custom Fee Rate')
@allure.story('Wallet Send Operation with Custom Fee Rate')
def test_send_bitcoin_with_custom_fee_rate(wallets_and_operations: WalletTestSetup):
    """Test sending bitcoin with a custom fee rate."""

    with allure.step('Fund First wallet'):
        wallets_and_operations.first_page_features.wallet_features.fund_wallet(
            FIRST_APPLICATION,
        )

    with allure.step('Get bitcoin address'):
        wallets_and_operations.second_page_operations.do_focus_on_application(
            SECOND_APPLICATION,
        )
        wallets_and_operations.second_page_objects.fungible_page_objects.click_bitcoin_frame()
        wallets_and_operations.second_page_objects.bitcoin_detail_page_objects.click_receive_bitcoin_button()
        address, copied_address = wallets_and_operations.second_page_features.receive_features.receive(
            application=SECOND_APPLICATION, transfer_type=TransferType.BITCOIN.value,
        )

    with allure.step('Verify address'):
        assert copied_address == address

    with allure.step('Send bitcoin with custom fee rate'):
        wallets_and_operations.first_page_operations.do_focus_on_application(
            FIRST_APPLICATION,
        )
        wallets_and_operations.first_page_objects.fungible_page_objects.click_bitcoin_frame()
        wallets_and_operations.first_page_objects.bitcoin_detail_page_objects.click_send_bitcoin_button()
        description = wallets_and_operations.first_page_features.send_features.send_with_custom_fee_rate(
            application=FIRST_APPLICATION, receiver_invoice=copied_address, amount=AMOUNT, fee_rate=FEE_RATE, transfer_type=TransferType.BITCOIN.value,
        )

    with allure.step('Refresh bitcoin page'):
        wallets_and_operations.second_page_operations.do_focus_on_application(
            SECOND_APPLICATION,
        )
        wallets_and_operations.second_page_objects.bitcoin_detail_page_objects.click_bitcoin_refresh_button()
        wallets_and_operations.second_page_objects.bitcoin_detail_page_objects.click_bitcoin_transaction_frame()
        tx_id = wallets_and_operations.second_page_objects.bitcoin_transaction_detail_page_objects.get_bitcoin_tx_id()

    with allure.step('Verify transaction id'):
        description = description.replace('Transaction Id: ', '')
        tx_id = re.sub(r'[\u200B\u200C\u200D\u2060\uFEFF]', '', tx_id)
        assert description == tx_id

    with allure.step('Close transaction detail page'):
        wallets_and_operations.second_page_objects.bitcoin_transaction_detail_page_objects.click_close_button()

    with allure.step('Close bitcoin detail page'):
        wallets_and_operations.second_page_objects.bitcoin_detail_page_objects.click_bitcoin_close_button()

    with allure.step('Close bitcoin detail page in first application'):
        wallets_and_operations.first_page_operations.do_focus_on_application(
            FIRST_APPLICATION,
        )
        wallets_and_operations.first_page_objects.bitcoin_detail_page_objects.click_bitcoin_close_button()


@allure.feature('Iris Wallet Send Operation with Invalid Invoice')
@allure.story('Wallet Send Operation with Invalid Invoice')
def test_send_bitcoin_with_invalid_invoice(wallets_and_operations: WalletTestSetup):
    """Test sending bitcoin with an invalid invoice."""

    with allure.step('Get asset from sidebar'):
        invoice = wallets_and_operations.second_page_features.receive_features.receive_asset_from_sidebar(
            SECOND_APPLICATION,
        )

    with allure.step('Send bitcoin with invalid invoice'):
        wallets_and_operations.first_page_operations.do_focus_on_application(
            FIRST_APPLICATION,
        )
        wallets_and_operations.first_page_objects.fungible_page_objects.click_bitcoin_frame()
        wallets_and_operations.first_page_objects.bitcoin_detail_page_objects.click_send_bitcoin_button()
        description = wallets_and_operations.first_page_features.send_features.send_with_wrong_invoice(
            application=FIRST_APPLICATION, receiver_invoice=invoice, amount=AMOUNT, transfer_type=TransferType.BITCOIN.value,
        )

    with allure.step('Verify error message'):
        assert description == SEND_BITCOIN_TOASTER_DESCRIPTION

    with allure.step('Close bitcoin detail page'):
        wallets_and_operations.first_page_objects.bitcoin_detail_page_objects.click_bitcoin_close_button()
