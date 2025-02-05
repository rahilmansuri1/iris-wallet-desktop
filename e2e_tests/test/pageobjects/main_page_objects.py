# pylint: disable = too-few-public-methods, too-many-instance-attributes
"""
Main Page Objects Module.
Contains MainPageObjects class for handling main page functionality.
"""
from __future__ import annotations

from e2e_tests.test.pageobjects.about_page import AboutPageObjects
from e2e_tests.test.pageobjects.asset_detail_page import AssetDetailPageObjects
from e2e_tests.test.pageobjects.bitcoin_detail_page import BitcoinDetailPageObjects
from e2e_tests.test.pageobjects.bitcoin_transaction_detail_page import BitcoinTransactionDetailPageObjects
from e2e_tests.test.pageobjects.channel_management_page import ChannelManagementPageObjects
from e2e_tests.test.pageobjects.collectible_page import CollectiblePageObjects
from e2e_tests.test.pageobjects.create_channel_page import CreateChannelPageObjects
from e2e_tests.test.pageobjects.create_ln_invoice_page import CreateLnInvoicePageObjects
from e2e_tests.test.pageobjects.fungible_page import FungiblePageObjects
from e2e_tests.test.pageobjects.issue_rgb20_page import IssueRgb20PageObjects
from e2e_tests.test.pageobjects.issue_rgb25_page import IssueRgb25PageObjects
from e2e_tests.test.pageobjects.receive_asset_page import ReceiveAssetPageObjects
from e2e_tests.test.pageobjects.send_asset_page import SendAssetPageObjects
from e2e_tests.test.pageobjects.send_ln_invoice_page import SendLnInvoicePageObjects
from e2e_tests.test.pageobjects.set_password_page import SetPasswordPageObjects
from e2e_tests.test.pageobjects.settings_page_object import SettingsPageObjects
from e2e_tests.test.pageobjects.sidebar_page import SidebarPageObjects
from e2e_tests.test.pageobjects.success_page import SuccessPageObjects
from e2e_tests.test.pageobjects.term_and_condition_page import TermAndConditionPageObjects
from e2e_tests.test.pageobjects.toaster_page import ToasterPageObjects
from e2e_tests.test.pageobjects.wallet_selection_page import WalletSelectionPageObjects
from e2e_tests.test.pageobjects.wallet_transfer_page import WalletTransferPageObjects
from e2e_tests.test.pageobjects.welcome_page import WelcomePageObjects


class MainPageObjects():
    """
    MainPageObjects class for handling main page functionality.
    """

    def __init__(self, application):
        """
        Initializes MainPageObjects instance.

        Args:
            application: The application instance.
        """
        self.application = application

        self.term_and_condition_page_objects = TermAndConditionPageObjects(
            self.application,
        )

        self.wallet_selection_page_objects = WalletSelectionPageObjects(
            self.application,
        )

        self.welcome_page_objects = WelcomePageObjects(self.application)

        self.set_password_page_objects = SetPasswordPageObjects(
            self.application,
        )

        self.fungible_page_objects = FungiblePageObjects(self.application)

        self.collectible_page_objects = CollectiblePageObjects(
            self.application,
        )

        self.bitcoin_detail_page_objects = BitcoinDetailPageObjects(
            self.application,
        )

        self.wallet_transfer_page_objects = WalletTransferPageObjects(
            self.application,
        )

        self.receive_asset_page_objects = ReceiveAssetPageObjects(
            self.application,
        )

        self.send_asset_page_objects = SendAssetPageObjects(self.application)

        self.issue_rgb20_page_objects = IssueRgb20PageObjects(self.application)

        self.success_page_objects = SuccessPageObjects(self.application)

        self.toaster_page_objects = ToasterPageObjects(self.application)

        self.sidebar_page_objects = SidebarPageObjects(self.application)

        self.issue_rgb25_page_objects = IssueRgb25PageObjects(self.application)

        self.asset_detail_page_objects = AssetDetailPageObjects(
            self.application,
        )

        self.send_ln_invoice_page_objects = SendLnInvoicePageObjects(
            self.application,
        )

        self.create_ln_invoice_page_objects = CreateLnInvoicePageObjects(
            self.application,
        )

        self.bitcoin_transaction_detail_page_objects = BitcoinTransactionDetailPageObjects(
            self.application,
        )

        self.create_channel_page_objects = CreateChannelPageObjects(
            self.application,
        )

        self.channel_management_page_objects = ChannelManagementPageObjects(
            self.application,
        )

        self.about_page_objects = AboutPageObjects(self.application)

        self.settings_page_objects = SettingsPageObjects(self.application)
