"""
Asset Transaction Detail Page Objects module.
"""
from __future__ import annotations

from accessible_constant import AMOUNT_VALUE
from accessible_constant import ASSET_TRANSACTION_DETAIL_CLOSE_BUTTON
from e2e_tests.test.utilities.base_operation import BaseOperations


class AssetTransactionDetailPageObjects(BaseOperations):
    """
    Asset Transaction Detail Page Objects class.
    """

    def __init__(self, application):
        """
        Initializes the AssetTransactionDetailPageObjects class.

        Args:
            application: The application instance.
        """
        super().__init__(application)

        self.transferred_amount = lambda: self.perform_action_on_element(
            role_name='label', description=AMOUNT_VALUE,
        )
        self.close_button = lambda: self.perform_action_on_element(
            role_name='push button', name=ASSET_TRANSACTION_DETAIL_CLOSE_BUTTON,
        )

    def get_transferred_amount(self):
        """
        Retrieves the transferred amount.

        Returns:
            The transferred amount if displayed, otherwise None.
        """
        return self.do_get_text(self.transferred_amount()) if self.do_is_displayed(self.transferred_amount()) else None

    def click_close_button(self):
        """
        Clicks the close button.

        Returns:
            The result of the click action if the button is displayed, otherwise None.
        """
        return self.do_click(self.close_button()) if self.do_is_displayed(self.close_button()) else None
