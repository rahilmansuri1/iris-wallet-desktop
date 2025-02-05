# pylint: disable=redefined-outer-name, unused-import
"""Tests for create channel"""
from __future__ import annotations

from accessible_constant import FIRST_APPLICATION
from accessible_constant import SECOND_APPLICATION
from e2e_tests.test.utilities.app_setup import test_environment
from e2e_tests.test.utilities.app_setup import wallets_and_operations

ASSET_TICKER = 'TTK'
ASSET_NAME = 'Tether'
ASSET_AMOUNT = '2000'
CREATE_ASSET_CHANNEL_WITH_AMOUNT = '100'
CHANNEL_CAPACITY = '30010'
IP_ADDRESS = '127.0.0.1'


def test_create_channel_with_actual_value(wallets_and_operations):
    """Test creating channel with actual value."""
    first_page_features, second_page_features, _, second_page_objects, first_page_operations, second_page_operations = wallets_and_operations

    first_page_features.wallet_features.create_embedded_wallet(
        FIRST_APPLICATION,
    )
    first_page_features.wallet_features.fund_wallet(FIRST_APPLICATION)

    second_page_features.wallet_features.create_embedded_wallet(
        SECOND_APPLICATION,
    )
    second_page_features.wallet_features.fund_wallet(SECOND_APPLICATION)

    first_page_operations.do_focus_on_application(FIRST_APPLICATION)
    first_page_features.issue_rgb20_features.issue_rgb20_with_sufficient_sats_and_utxo(
        application=FIRST_APPLICATION, asset_ticker=ASSET_TICKER, asset_name=ASSET_NAME, asset_amount=ASSET_AMOUNT,
    )

    second_page_operations.do_focus_on_application(SECOND_APPLICATION)
    second_page_objects.sidebar_page_objects.click_about_button()
    second_page_objects.about_page_objects.click_node_pubkey_button()
    node_pubkey = second_page_objects.about_page_objects.do_get_copied_address()
    second_page_objects.about_page_objects.click_ln_peer_listening_port_copy_button()
    ln_port = second_page_objects.about_page_objects.do_get_copied_address()
    node_uri = f"{node_pubkey}@{IP_ADDRESS}:{ln_port}"

    first_page_operations.do_focus_on_application(FIRST_APPLICATION)
    first_page_features.create_channel_features.create_channel(
        application=FIRST_APPLICATION, node_uri=node_uri, asset_ticker=ASSET_TICKER, asset_amount=CREATE_ASSET_CHANNEL_WITH_AMOUNT, channel_capacity=CHANNEL_CAPACITY,
    )
