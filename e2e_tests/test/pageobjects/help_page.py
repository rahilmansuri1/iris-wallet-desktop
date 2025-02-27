"""
Help Page Objects class for interacting with the application.
"""
from __future__ import annotations

from accessible_constant import HELP_CARD_TITLE_ACCESSIBLE_DESCRIPTION
from e2e_tests.test.utilities.base_operation import BaseOperations


class HelpPageObjects(BaseOperations):
    """Help Page Objects class."""

    def __init__(self, application):
        """
        Initializes the HelpPageObjects class with the application.

        Args:
            application: The application instance.
        """
        super().__init__(application)
        self.testnet_bitcoin_frame_title = lambda: self.perform_action_on_element(
            role_name='label', description=HELP_CARD_TITLE_ACCESSIBLE_DESCRIPTION+'_1',
        )
        self.bitcoin_txn_frame_label = lambda: self.perform_action_on_element(
            role_name='label', description=HELP_CARD_TITLE_ACCESSIBLE_DESCRIPTION+'_2',
        )

    def click_testnet_bitcoin(self):
        """Clicks on testnet bitcoin frame"""
        return self.do_click(self.testnet_bitcoin_frame_title()) if self.do_is_displayed(self.testnet_bitcoin_frame_title()) else None

    def click_bitcoin_txn(self):
        """Clicks on bitcoin transaction frame"""
        return self.do_click(self.bitcoin_txn_frame_label()) if self.do_is_displayed(self.bitcoin_txn_frame_label()) else None

    def get_testnet_bitcoin_frame_title(self):
        """Returns the title of testnet bitcoin frame"""
        return self.do_get_text(self.testnet_bitcoin_frame_title()) if self.do_is_displayed(self.testnet_bitcoin_frame_title()) else None

    def get_bitcoin_txn_frame_label(self):
        """Returns the label of bitcoin transaction frame"""
        return self.do_get_text(self.bitcoin_txn_frame_label()) if self.do_is_displayed(self.bitcoin_txn_frame_label()) else None
