"""
Term and Condition Page Objects Module.
"""
from __future__ import annotations

from accessible_constant import ACCEPT_BUTTON
from accessible_constant import DECLINE_BUTTON
from e2e_tests.test.utilities.base_operation import BaseOperations


class TermAndConditionPageObjects(BaseOperations):
    """
    Term and Condition Page Objects class.
    """

    def __init__(self, application):
        """
        Initializes the TermAndConditionPageObjects class.

        Args:
            application: The application instance.
        """
        super().__init__(application)

        # Lazy evaluation of elements using lambdas
        self.accept_button = lambda: self.perform_action_on_element(
            role_name='push button', name=ACCEPT_BUTTON,
        )
        self.decline_button = lambda: self.perform_action_on_element(
            role_name='push button', name=DECLINE_BUTTON,
        )
        self.title = lambda: self.perform_action_on_element(
            role_name='label', name='Terms and Conditions',
        )

    def click_accept_button(self):
        """
        Clicks the accept button if it is displayed.

        Returns:
            The result of the click action or None if the button is not displayed.
        """
        return self.do_click(self.accept_button()) if self.do_is_displayed(self.accept_button()) else None

    def click_decline_button(self):
        """
        Clicks the decline button if it is displayed.

        Returns:
            The result of the click action or None if the button is not displayed.
        """
        return self.do_click(self.decline_button()) if self.do_is_displayed(self.decline_button()) else None
