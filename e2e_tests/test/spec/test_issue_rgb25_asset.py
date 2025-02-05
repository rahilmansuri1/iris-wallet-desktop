# pylint: disable=redefined-outer-name, unused-import
"""
Tests for issuing rgb25 assets with different scenarios.
"""
from __future__ import annotations

import allure
import pytest

from accessible_constant import FIRST_APPLICATION
from e2e_tests.test.utilities.app_setup import test_environment
from e2e_tests.test.utilities.app_setup import wallets_and_operations

ASSET_NAME = 'Rgb25'
ASSET_DESCRIPTION = 'This is Rgb25 asset'
ASSET_AMOUNT = '2000'
ISSUE_RGB25_TOASTER_MESSAGE = 'You have insufficient funds'


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('Issue rgb25 asset without sufficient sats')
@allure.story('Issue rgb25 asset without sufficient sats which will produce error toaster')
def test_issue_rgb25_without_sufficient_sats(wallets_and_operations):
    """
    Test issuing rgb25 asset without sufficient sats.
    """
    first_page_features, _, _, _, _, _ = wallets_and_operations

    with allure.step('Create embedded wallet'):
        first_page_features.wallet_features.create_embedded_wallet(
            FIRST_APPLICATION,
        )

    with allure.step('Issue rgb25 asset without sat'):
        description = first_page_features.issue_rgb25_features.issue_rgb25_asset_without_sat(
            FIRST_APPLICATION, ASSET_NAME, ASSET_DESCRIPTION, ASSET_AMOUNT,
        )

    with allure.step('Verify toaster title and message'):
        assert description == ISSUE_RGB25_TOASTER_MESSAGE


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('Issue rgb25 asset with sufficient sats but no utxo')
@allure.story('Issue rgb25 asset with sufficient sats and no utxo which will first create utxo and then create asset')
def test_issue_rgb25_with_sufficient_sats_and_no_utxo(wallets_and_operations):
    """
    Test issuing rgb25 asset with sufficient sats but no utxo.
    """
    first_page_features, _, first_page_objects, _, _, _ = wallets_and_operations

    with allure.step('Fund wallet'):
        first_page_features.wallet_features.fund_wallet(FIRST_APPLICATION)

    with allure.step('Issue rgb25 with sufficient sats and no utxo'):
        first_page_features.issue_rgb25_features.issue_rgb25_with_sufficient_sats_and_no_utxo(
            FIRST_APPLICATION, ASSET_NAME, ASSET_DESCRIPTION, ASSET_AMOUNT,
        )

    with allure.step('Verify asset name'):
        asset_name = first_page_objects.collectible_page_objects.get_rgb25_asset_name(
            ASSET_NAME,
        )
        assert asset_name == ASSET_NAME


@pytest.mark.parametrize('test_environment', [False], indirect=True)
@allure.feature('Issue rgb25 asset with sufficient sats and utxo')
@allure.story('Issue rgb25 asset with sufficient sats and utxo which will create asset')
def test_issue_rgb25_with_sufficient_sats_and_utxo(wallets_and_operations):
    """
    Test issuing rgb25 asset with sufficient sats and utxo.
    """
    first_page_features, _, first_page_objects, _, _, _ = wallets_and_operations

    with allure.step('Issue rgb25 with sufficient sats and utxo'):
        first_page_features.issue_rgb25_features.issue_rgb25_with_sufficient_sats_and_utxo(
            FIRST_APPLICATION, ASSET_NAME, ASSET_DESCRIPTION, ASSET_AMOUNT,
        )

    with allure.step('Verify asset name'):
        asset_name = first_page_objects.collectible_page_objects.get_rgb25_asset_name(
            ASSET_NAME,
        )
        assert asset_name == ASSET_NAME
