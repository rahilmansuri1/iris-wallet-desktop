# pylint: disable=redefined-outer-name, unused-import
"""Iris Wallet Send and Receive Operation Automation Test Suite for Bitcoin.
Test suite for Iris Wallet's send and receive operations with Bitcoin."""
from __future__ import annotations

import re

import allure

from accessible_constant import FIRST_APPLICATION
from accessible_constant import SECOND_APPLICATION
from e2e_tests.test.utilities.app_setup import test_environment
from e2e_tests.test.utilities.app_setup import wallets_and_operations
AMOUNT = '50000000'
AVAILABLE_BALANCE = '49999347'
AMOUNT_VALIDATION = 'The payment amount exceeds the spendable balance'
SEND_BITCOIN_TOASTER_DESCRIPTION = 'The address is invalid'
FEE_RATE = '8'


@allure.feature('Iris Wallet Send operation with zero balance')
@allure.story('Wallet send operation with zero balance which will give error label')
def test_send_bitcoin_with_zero_balance(wallets_and_operations):
    """Test sending bitcoin with zero balance."""
    first_page_features, _, first_page_objects, _, _, _ = wallets_and_operations
    with allure.step('Create embedded wallet'):
        first_page_features.wallet_features.create_embedded_wallet(
            FIRST_APPLICATION,
        )

    with allure.step('Get bitcoin address'):
        first_page_objects.fungible_page_objects.click_bitcoin_frame()
        first_page_objects.bitcoin_detail_page_objects.click_receive_bitcoin_button()
        address, copied_address = first_page_features.receive_features.receive(
            application=FIRST_APPLICATION, transfer_type='bitcoin',
        )

    with allure.step('Verify address'):
        assert copied_address == address

    with allure.step('Send bitcoin with zero balance'):
        first_page_objects.bitcoin_detail_page_objects.click_send_bitcoin_button()
        validation = first_page_features.send_features.send_with_no_fund(
            application=FIRST_APPLICATION, receiver_invoice=copied_address, amount=AMOUNT, transfer_type='bitcoin',
        )

    with allure.step('Verify error message'):
        assert validation == AMOUNT_VALIDATION

    with allure.step('Close bitcoin detail page'):
        first_page_objects.bitcoin_detail_page_objects.click_bitcoin_close_button()


@allure.feature('Iris Wallet Receive and Send Operation Automation for bitcoin')
@allure.story('Wallet Receive and Send Operation Automation for bitcoin')
def test_receive_and_send_bitcoin(wallets_and_operations):
    """Test receiving and sending bitcoin."""
    first_page_features, second_page_features, first_page_objects, second_page_objects, first_operations, second_operations = wallets_and_operations
    with allure.step('Create embedded wallet'):
        first_page_features.wallet_features.fund_wallet(FIRST_APPLICATION)
        second_page_features.wallet_features.create_embedded_wallet(
            SECOND_APPLICATION,
        )

    with allure.step('Get bitcoin address'):
        second_operations.do_focus_on_application(SECOND_APPLICATION)
        second_page_objects.fungible_page_objects.click_bitcoin_frame()
        second_page_objects.bitcoin_detail_page_objects.click_receive_bitcoin_button()
        address, copied_address = second_page_features.receive_features.receive(
            application=SECOND_APPLICATION, transfer_type='bitcoin',
        )

    with allure.step('Verify address'):
        assert copied_address == address

    with allure.step('Send bitcoin'):
        first_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.fungible_page_objects.click_bitcoin_frame()
        first_page_objects.bitcoin_detail_page_objects.click_send_bitcoin_button()
        first_page_features.send_features.send(
            application=FIRST_APPLICATION, receiver_invoice=copied_address, amount=AMOUNT, transfer_type='bitcoin',
        )

    with allure.step('Refresh bitcoin page'):
        second_operations.do_focus_on_application(SECOND_APPLICATION)
        second_page_objects.bitcoin_detail_page_objects.click_bitcoin_refresh_button()

    with allure.step('Verify received balance'):
        received_balance = second_page_objects.bitcoin_detail_page_objects.get_total_balance()
        received_balance = received_balance.replace(' SATS', '')
        assert received_balance == AMOUNT

    with allure.step('Close bitcoin detail page'):
        second_page_objects.bitcoin_detail_page_objects.click_bitcoin_close_button()

    with allure.step('Verify balance in first application'):
        first_operations.do_focus_on_application(FIRST_APPLICATION)
        available_balance = first_page_objects.bitcoin_detail_page_objects.get_total_balance()
        available_balance = available_balance.replace(' SATS', '')
        assert available_balance == AVAILABLE_BALANCE

    with allure.step('Close bitcoin detail page in first application'):
        first_page_objects.bitcoin_detail_page_objects.click_bitcoin_close_button()


@allure.feature('Iris Wallet Send Operation with Custom Fee Rate')
@allure.story('Wallet Send Operation with Custom Fee Rate')
def test_send_bitcoin_with_custom_fee_rate(wallets_and_operations):
    """Test sending bitcoin with a custom fee rate."""
    first_page_features, second_page_features, first_page_objects, second_page_objects, first_operations, second_operations = wallets_and_operations
    with allure.step('Fund wallet'):
        first_page_features.wallet_features.fund_wallet(FIRST_APPLICATION)

    with allure.step('Get bitcoin address'):
        second_operations.do_focus_on_application(SECOND_APPLICATION)
        second_page_objects.fungible_page_objects.click_bitcoin_frame()
        second_page_objects.bitcoin_detail_page_objects.click_receive_bitcoin_button()
        address, copied_address = second_page_features.receive_features.receive(
            application=SECOND_APPLICATION, transfer_type='bitcoin',
        )

    with allure.step('Verify address'):
        assert copied_address == address

    with allure.step('Send bitcoin with custom fee rate'):
        first_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.fungible_page_objects.click_bitcoin_frame()
        first_page_objects.bitcoin_detail_page_objects.click_send_bitcoin_button()
        description = first_page_features.send_features.send_with_custom_fee_rate(
            application=FIRST_APPLICATION, receiver_invoice=copied_address, amount=AMOUNT, fee_rate=FEE_RATE, transfer_type='bitcoin',
        )

    with allure.step('Refresh bitcoin page'):
        second_operations.do_focus_on_application(SECOND_APPLICATION)
        second_page_objects.bitcoin_detail_page_objects.click_bitcoin_refresh_button()
        second_page_objects.bitcoin_detail_page_objects.click_bitcoin_transaction_frame()
        tx_id = second_page_objects.bitcoin_transaction_detail_page_objects.get_bitcoin_tx_id()

    with allure.step('Verify transaction id'):
        description = description.replace('Transaction Id: ', '')
        tx_id = re.sub(r'[\u200B\u200C\u200D\u2060\uFEFF]', '', tx_id)
        assert description == tx_id

    with allure.step('Close transaction detail page'):
        second_page_objects.bitcoin_transaction_detail_page_objects.click_close_button()

    with allure.step('Close bitcoin detail page'):
        second_page_objects.bitcoin_detail_page_objects.click_bitcoin_close_button()

    with allure.step('Close bitcoin detail page in first application'):
        first_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.bitcoin_detail_page_objects.click_bitcoin_close_button()


@allure.feature('Iris Wallet Send Operation with Invalid Invoice')
@allure.story('Wallet Send Operation with Invalid Invoice')
def test_send_bitcoin_with_invalid_invoice(wallets_and_operations):
    """Test sending bitcoin with an invalid invoice."""
    first_page_features, second_page_features, first_page_objects, _, first_page_operations, _ = wallets_and_operations

    with allure.step('Get asset from sidebar'):
        invoice = second_page_features.receive_features.receive_asset_from_sidebar(
            SECOND_APPLICATION,
        )

    with allure.step('Send bitcoin with invalid invoice'):
        first_page_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.fungible_page_objects.click_bitcoin_frame()
        first_page_objects.bitcoin_detail_page_objects.click_send_bitcoin_button()
        description = first_page_features.send_features.send_with_wrong_invoice(
            application=FIRST_APPLICATION, receiver_invoice=invoice, amount=AMOUNT, transfer_type='bitcoin',
        )

    with allure.step('Verify error message'):
        assert description == SEND_BITCOIN_TOASTER_DESCRIPTION

    with allure.step('Close bitcoin detail page'):
        first_page_objects.bitcoin_detail_page_objects.click_bitcoin_close_button()
