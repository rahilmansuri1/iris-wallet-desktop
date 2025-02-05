"""
Wallet Selection Page Objects Module.
"""
from __future__ import annotations

from accessible_constant import OPTION_1_FRAME
from accessible_constant import OPTION_2_FRAME
from e2e_tests.test.utilities.base_operation import BaseOperations


class WalletSelectionPageObjects(BaseOperations):
    """
    Wallet Selection Page Objects class.
    """

    def __init__(self, application):
        """
        Initializes the WalletSelectionPageObjects class.

        Args:
            application: The application instance.
        """
        super().__init__(application)

        # Lazy evaluation of elements using lambdas
        self.embedded_button = lambda: self.perform_action_on_element(
            role_name='panel', name=OPTION_1_FRAME,
        )
        self.connect_button = lambda: self.perform_action_on_element(
            role_name='panel', name=OPTION_2_FRAME,
        )

    def click_embedded_button(self):
        """
        Clicks the embedded button if it is displayed.

        Returns:
            The result of the click action or None if the button is not displayed.
        """
        return self.do_click(self.embedded_button()) if self.do_is_displayed(self.embedded_button()) else None

    def click_connect_button(self):
        """
        Clicks the connect button if it is displayed.

        Returns:
            The result of the click action or None if the button is not displayed.
        """
        return self.do_click(self.connect_button()) if self.do_is_displayed(self.connect_button()) else None
