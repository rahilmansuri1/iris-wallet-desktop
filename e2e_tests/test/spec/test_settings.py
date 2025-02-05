# pylint: disable=redefined-outer-name, unused-import
"""Test module for the settings page functionality"""
from __future__ import annotations

import allure
import pytest

from accessible_constant import FIRST_APPLICATION
from e2e_tests.test.utilities.app_setup import test_environment
from e2e_tests.test.utilities.app_setup import wallets_and_operations

TEST_ANNOUNCE_ADDRESS = 'example.url.com:2222'
TEST_ANNOUNCE_ALIAS = 'testAlias'
TEST_INVALID_ANNOUNCE_ADDRESS = 'example'
TEST_INDEXER_URL = 'electrum.rgbtools.org:50041'
TEST_INVALID_INDEXER_URL = 'test.indexer'
TEST_RGB_PROXY_URL = 'rpcs://proxy.iriswallet.com/0.2/json-rpc'
TEST_INVALID_RGB_PROXY_URL = 'test.rgb.proxy'
TEST_INVALID_BITCOIND_HOST = 'test.bitcoind.host'
TEST_INVALID_BITCOIND_PORT = '42069'
TEST_FEE_RATE = '20'
TEST_FEE_RATE_TOAST_DESC_SUCCESS = 'Fee rate set successfully'


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('Set Default Fee Rate')
@allure.story('Sets Default Fee Rate For Sending Assets')
def test_set_default_fee_rate(wallets_and_operations):
    """Test setting a default fee rate

    Tests that a user can:
    1. Navigate to settings
    2. Set a new default fee rate
    3. Verify the fee rate is saved and applied
    """
    with allure.step('Launching app and initializing the wallet'):
        first_page_features, _, first_page_objects, __, first_page_operations, ___ = wallets_and_operations
        first_page_features.wallet_features.create_embedded_wallet(
            FIRST_APPLICATION,
        )

    with allure.step('Navigating to set default fee rate frame in settings'):
        first_page_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.sidebar_page_objects.click_settings_button()
        first_page_objects.settings_page_objects.click_default_fee_rate_frame()

    with allure.step('Entering a new default fee rate and saving'):
        first_page_objects.settings_page_objects.clear_default_fee_rate()
        first_page_objects.settings_page_objects.enter_new_default_fee_rate(
            TEST_FEE_RATE,
        )
        first_page_objects.settings_page_objects.click_save_button()
        first_page_objects.toaster_page_objects.click_toaster_frame()
        toast_description = first_page_objects.toaster_page_objects.get_toaster_description()

    assert toast_description == TEST_FEE_RATE_TOAST_DESC_SUCCESS

    with allure.step('Navigating to Send Bitcoin page to see the new default fee rate'):
        first_page_objects.sidebar_page_objects.click_fungibles_button()
        first_page_objects.fungible_page_objects.click_bitcoin_frame()
        first_page_objects.bitcoin_detail_page_objects.click_send_bitcoin_button()
        first_page_objects.wallet_transfer_page_objects.click_on_chain_button()
        new_default_fee_rate = first_page_objects.send_asset_page_objects.get_fee_rate_text()

    assert new_default_fee_rate == TEST_FEE_RATE

    with allure.step('Navigating back to Fungibles page'):
        first_page_objects.send_asset_page_objects.click_send_asset_close_button()
        first_page_objects.bitcoin_detail_page_objects.click_bitcoin_close_button()


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('Set Announce Address')
@allure.story('Setting an Announce address for this')
@allure.description('Testing with an invalid announce address')
def test_set_valid_announce_address(wallets_and_operations):
    """Test setting a valid announce address

    Tests that a user can:
    1. Navigate to settings
    2. Set a valid announce address
    3. Verify the address is saved correctly
    """
    with allure.step('Initializing the wallet'):
        _, _, first_page_objects, _, first_operations, _ = wallets_and_operations

    with allure.step('Navigating to Set Announce Address frame'):
        first_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.sidebar_page_objects.click_settings_button()
        first_page_objects.settings_page_objects.click_specify_announce_address_frame()

    with allure.step('Enter a New Announce Address'):
        first_page_objects.settings_page_objects.clear_announce_address()
        first_page_objects.settings_page_objects.enter_new_announce_address(
            TEST_ANNOUNCE_ADDRESS,
        )
        first_page_objects.settings_page_objects.click_save_button()

        first_page_objects.toaster_page_objects.click_toaster_frame()
        announce_add_toast_desc = first_page_objects.toaster_page_objects.get_toaster_description()

    assert announce_add_toast_desc == 'Announce address set successfully.'

    with allure.step('Navigating to About page'):
        first_page_objects.sidebar_page_objects.click_about_button()
        test_announce_address = first_page_objects.about_page_objects.get_announce_address()

    assert test_announce_address == TEST_ANNOUNCE_ADDRESS

    with allure.step('Navigating back to Fungibles page'):
        first_page_objects.sidebar_page_objects.click_fungibles_button()


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('Set Announce Alias')
@allure.story('Setting an Announce alias for this')
def test_set_announce_alias(wallets_and_operations):
    """Test setting an announce alias

    Tests that a user can:
    1. Navigate to settings
    2. Set an announce alias
    3. Verify the alias is saved correctly
    """
    with allure.step('Initializing the wallet'):
        _, _, first_page_objects, _, first_operations, _ = wallets_and_operations

    with allure.step('Navigating to Set Announce Alias frame'):
        first_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.sidebar_page_objects.click_settings_button()
        first_page_objects.settings_page_objects.click_specify_announce_alias()

    with allure.step('Enter a New Announce Alias'):
        first_page_objects.settings_page_objects.clear_announce_alias()
        first_page_objects.settings_page_objects.enter_new_announce_alias(
            TEST_ANNOUNCE_ALIAS,
        )
        first_page_objects.settings_page_objects.click_save_button()

        first_page_objects.toaster_page_objects.click_toaster_frame()
        announce_add_toast_desc = first_page_objects.toaster_page_objects.get_toaster_description()

    assert announce_add_toast_desc == 'Announce alias set successfully.'

    with allure.step('Navigating to About page'):
        first_page_objects.sidebar_page_objects.click_about_button()
        test_announce_address = first_page_objects.about_page_objects.get_announce_alias()

    assert test_announce_address == TEST_ANNOUNCE_ALIAS

    with allure.step('Navigating to Fungibles page'):
        first_page_objects.sidebar_page_objects.click_fungibles_button()


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('Set Indexer URL')
@allure.story('Setting an indexer url for the wallet')
def test_set_valid_electrum_url(wallets_and_operations):
    """Test setting a valid electrum URL

    Tests that a user can:
    1. Navigate to settings
    2. Set a valid electrum URL
    3. Verify the URL is saved correctly
    """
    with allure.step('Initializing the wallet'):
        _, _, first_page_objects, _, first_operations, _ = wallets_and_operations

    with allure.step('Navigating to Set Electrum URL frame'):
        first_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.sidebar_page_objects.click_settings_button()
        first_page_objects.settings_page_objects.click_set_indexer_url_frame()

    with allure.step('Enter a New Electrum URL'):
        first_page_objects.settings_page_objects.clear_indexer_url()
        first_page_objects.settings_page_objects.enter_new_indexer_url(
            TEST_INDEXER_URL,
        )
        first_page_objects.settings_page_objects.click_save_button()

        first_page_objects.toaster_page_objects.click_toaster_frame()
        announce_add_toast_desc = first_page_objects.toaster_page_objects.get_toaster_description()

    assert announce_add_toast_desc == 'Indexer url set successfully.'

    with allure.step('Navigating to About page'):
        first_page_objects.sidebar_page_objects.click_about_button()
        test_announce_address = first_page_objects.about_page_objects.get_indexer_url()

    assert test_announce_address == TEST_INDEXER_URL

    with allure.step('Navigating to Fungibles page'):
        first_page_objects.sidebar_page_objects.click_fungibles_button()


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('Set Indexer URL')
@allure.story('Setting an invalid indexer url for the wallet')
def test_set_invalid_electrum_url(wallets_and_operations):
    """Test setting an invalid electrum URL

    Tests that when a user:
    1. Navigates to settings
    2. Attempts to set an invalid electrum URL
    3. The system shows appropriate error message
    """
    with allure.step('Initializing the wallet'):
        _, _, first_page_objects, _, first_operations, _ = wallets_and_operations

    with allure.step('Navigating to Set Electrum URL frame'):
        first_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.sidebar_page_objects.click_settings_button()
        first_page_objects.settings_page_objects.click_set_indexer_url_frame()

    with allure.step('Enter a New Electrum URL'):
        first_page_objects.settings_page_objects.clear_indexer_url()
        first_page_objects.settings_page_objects.enter_new_indexer_url(
            TEST_INVALID_INDEXER_URL,
        )
        first_page_objects.settings_page_objects.click_save_button()

        first_page_objects.toaster_page_objects.click_toaster_frame()
        announce_add_toast_desc = first_page_objects.toaster_page_objects.get_toaster_description()

    assert announce_add_toast_desc == 'The indexer is invalid'

    with allure.step('Navigating to Fungibles page'):
        first_page_objects.sidebar_page_objects.click_fungibles_button()


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('Set RGB Proxy URL')
@allure.story('Setting a RGB proxy url for the wallet')
def test_set_rgb_proxy_url(wallets_and_operations):
    """Test setting a valid RGB proxy URL

    Tests that a user can:
    1. Navigate to settings
    2. Set a valid RGB proxy URL
    3. Verify the URL is saved correctly
    """
    with allure.step('Initializing the wallet'):
        _, _, first_page_objects, _, first_operations, _ = wallets_and_operations

    with allure.step('Navigating to Set RGB Proxy URL frame'):
        first_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.sidebar_page_objects.click_settings_button()
        first_page_objects.settings_page_objects.click_set_rgb_proxy_url_frame()

    with allure.step('Enter a New RGB Proxy URL'):
        first_page_objects.settings_page_objects.clear_rgb_proxy_url_frame()
        first_page_objects.settings_page_objects.enter_new_rgb_proxy_url(
            TEST_RGB_PROXY_URL,
        )
        first_page_objects.settings_page_objects.click_save_button()

        first_page_objects.toaster_page_objects.click_toaster_frame()
        announce_add_toast_desc = first_page_objects.toaster_page_objects.get_toaster_description()

    assert announce_add_toast_desc == 'Proxy endpoint set successfully.'

    with allure.step('Navigating to About page to see the changes'):
        first_page_objects.sidebar_page_objects.click_about_button()
        proxy_url = first_page_objects.about_page_objects.get_rgb_proxy_url()

    assert proxy_url == TEST_RGB_PROXY_URL

    with allure.step('Navigating to Fungibles page'):
        first_page_objects.sidebar_page_objects.click_fungibles_button()


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('Set RGB Proxy URL')
@allure.story('Setting an invalid RGB proxy url for the wallet')
def test_set_invalid_rgb_proxy_url(wallets_and_operations):
    """Test setting an invalid RGB proxy URL

    Tests that when a user:
    1. Navigates to settings
    2. Attempts to set an invalid RGB proxy URL
    3. The system shows appropriate error message
    """
    with allure.step('Initializing the wallet'):
        _, _, first_page_objects, _, first_operations, _ = wallets_and_operations

    with allure.step('Navigating to Set RGB Proxy URL frame'):
        first_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.sidebar_page_objects.click_settings_button()
        first_page_objects.settings_page_objects.click_set_rgb_proxy_url_frame()

    with allure.step('Enter an invalid RGB Proxy URL'):
        first_page_objects.settings_page_objects.clear_rgb_proxy_url_frame()
        first_page_objects.settings_page_objects.enter_new_rgb_proxy_url(
            TEST_INVALID_RGB_PROXY_URL,
        )
        first_page_objects.settings_page_objects.click_save_button()

        first_page_objects.toaster_page_objects.click_toaster_frame()
        announce_add_toast_desc = first_page_objects.toaster_page_objects.get_toaster_description()

    assert announce_add_toast_desc == 'The proxy endpoint is invalid'

    with allure.step('Navigating to Fungibles page'):
        first_page_objects.sidebar_page_objects.click_fungibles_button()


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('Set a Bitcoind host')
@allure.story('Setting an invalid bitcoind host for the wallet')
def test_set_invalid_bitcoind_host(wallets_and_operations):
    """Test setting an invalid bitcoind host

    Tests that when a user:
    1. Navigates to settings
    2. Attempts to set an invalid bitcoind host
    3. The system shows appropriate error message
    """
    with allure.step('Initializing the wallet'):
        _, _, first_page_objects, _, first_operations, _ = wallets_and_operations

    with allure.step('Navigating to set bitcoind host frame'):
        first_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.sidebar_page_objects.click_settings_button()
        first_page_objects.settings_page_objects.click_specify_bitcoind_host_frame()

    with allure.step('Enter an invalid bitcoind host'):
        first_page_objects.settings_page_objects.clear_bitcoind_host()
        first_page_objects.settings_page_objects.enter_new_bitcoind_host(
            TEST_INVALID_BITCOIND_HOST,
        )
        first_page_objects.settings_page_objects.click_save_button()

        first_page_objects.toaster_page_objects.click_toaster_frame()
        announce_add_toast_desc = first_page_objects.toaster_page_objects.get_toaster_description()

    assert announce_add_toast_desc == 'Unlock failed: Unable to connect to the Bitcoin daemon'

    with allure.step('Navigating to Fungibles page'):
        first_page_objects.sidebar_page_objects.click_fungibles_button()


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('Set a Bitcoind Port')
@allure.story('Setting an invalid bitcoind port for the wallet')
def test_set_invalid_bitcoind_port(wallets_and_operations):
    """Test setting an invalid bitcoind port

    Tests that when a user:
    1. Navigates to settings
    2. Attempts to set an invalid bitcoind port
    3. The system shows appropriate error message
    """
    with allure.step('Initializing the wallet'):
        _, _, first_page_objects, _, first_operations, _ = wallets_and_operations

    with allure.step('Navigating to set bitcoind port frame'):
        first_operations.do_focus_on_application(FIRST_APPLICATION)
        first_page_objects.sidebar_page_objects.click_settings_button()
        first_page_objects.settings_page_objects.click_specify_bitcoind_port_frame()

    with allure.step('Enter an invalid bitcoind port'):
        first_page_objects.settings_page_objects.clear_bitcoind_port()
        first_page_objects.settings_page_objects.enter_new_bitcoind_port(
            TEST_INVALID_BITCOIND_PORT,
        )
        first_page_objects.settings_page_objects.click_save_button()

        first_page_objects.toaster_page_objects.click_toaster_frame()
        announce_add_toast_desc = first_page_objects.toaster_page_objects.get_toaster_description()

    assert announce_add_toast_desc == 'Unlock failed: Unable to connect to the Bitcoin daemon'

    with allure.step('Navigating to Fungibles page'):
        first_page_objects.sidebar_page_objects.click_fungibles_button()
