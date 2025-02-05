"""
Fungible Page Objects class for interacting with the application.
"""
from __future__ import annotations

from accessible_constant import ISSUE_RGB20_ASSET
from e2e_tests.test.utilities.base_operation import BaseOperations


class FungiblePageObjects(BaseOperations):
    """Fungible Page Objects class."""

    def __init__(self, application):
        """
        Initializes the FungiblePageObjects class with the application.

        Args:
            application: The application instance.
        """
        super().__init__(application)

        # Define elements using lambdas for lazy evaluation
        self.rgb_20_asset_name = None
        self.issue_rgb20_button = lambda: self.perform_action_on_element(
            role_name='push button', name=ISSUE_RGB20_ASSET,
        )
        self.bitcoin_frame = lambda: self.perform_action_on_element(
            role_name='label', name='regtest bitcoin',
        )

    def click_issue_rgb20_button(self):
        """
        Clicks the issue RGB20 button if it is displayed.

        Returns:
            bool: True if the button is clicked, None otherwise.
        """
        return self.do_click(self.issue_rgb20_button()) if self.do_is_displayed(self.issue_rgb20_button()) else None

    def click_bitcoin_frame(self):
        """
        Clicks the bitcoin frame if it is displayed.

        Returns:
            bool: True if the frame is clicked, None otherwise.
        """
        return self.do_click(self.bitcoin_frame()) if self.do_is_displayed(self.bitcoin_frame()) else None

    def get_rgb20_asset_name(self, asset_name):
        """
        Retrieves the asset name if it is displayed.

        Args:
            asset_name (str): The name of the asset.

        Returns:
            str: The asset name if it is displayed, None otherwise.
        """
        self.rgb_20_asset_name = self.perform_action_on_element(
            role_name='label', name=asset_name,
        )
        return self.do_get_text(self.rgb_20_asset_name) if self.do_is_displayed(self.rgb_20_asset_name) else None

    def click_rgb20_frame(self, asset_name):
        """
        Clicks the RGB20 frame if it is displayed.

        Args:
            asset_name (str): The name of the asset.

        Returns:
            bool: True if the frame is clicked, None otherwise.
        """
        self.rgb_20_asset_name = self.perform_action_on_element(
            role_name='label', name=asset_name,
        )
        return self.do_click(self.rgb_20_asset_name) if self.do_is_displayed(self.rgb_20_asset_name) else None
