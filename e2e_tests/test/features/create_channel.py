"""
This module contains the IssueRgb20 class, which provides methods for issuing RGB20 assets.
"""
from __future__ import annotations

from dogtail.rawinput import keyCombo
from dogtail.rawinput import typeText

from e2e_tests.test.pageobjects.main_page_objects import MainPageObjects
from e2e_tests.test.utilities.base_operation import BaseOperations
from e2e_tests.test.utilities.executable_shell_script import mine


class CreateChannel(MainPageObjects, BaseOperations):
    """This class represents the create channel feature"""

    def __init__(self, application):
        super().__init__(application)

    def create_channel(self, application, node_uri, asset_ticker, asset_amount, channel_capacity):
        """
        This method creates a new channel with the given name.
        """
        self.do_focus_on_application(application)
        if self.do_is_displayed(self.sidebar_page_objects.channel_management_button()):
            self.sidebar_page_objects.click_channel_management_button()

        if self.do_is_displayed(self.channel_management_page_objects.create_channel_button()):
            self.channel_management_page_objects.click_create_channel_button()

        if self.do_is_displayed(self.create_channel_page_objects.node_uri_input()):
            self.create_channel_page_objects.enter_node_uri_input(node_uri)

        if self.do_is_displayed(self.create_channel_page_objects.channel_next_button()):
            self.create_channel_page_objects.click_channel_next_button()

        if self.do_is_displayed(self.create_channel_page_objects.channel_combobox()):
            self.create_channel_page_objects.click_channel_combobox()
            typeText(asset_ticker)
            keyCombo('enter')

        if self.do_is_displayed(self.create_channel_page_objects.channel_asset_amount()):
            self.create_channel_page_objects.enter_channel_asset_amount(
                asset_amount,
            )

        if self.do_is_displayed(self.create_channel_page_objects.channel_capacity_sat()):
            self.create_channel_page_objects.enter_channel_capacity_sat(
                channel_capacity,
            )

        if self.do_is_displayed(self.create_channel_page_objects.channel_next_button()):
            self.create_channel_page_objects.click_channel_next_button()

        if self.do_is_displayed(self.success_page_objects.home_button()):
            self.success_page_objects.click_home_button()

        mine(6)

        if self.do_is_displayed(self.channel_management_page_objects.refresh_button()):
            self.channel_management_page_objects.click_refresh_button()

        if self.do_is_displayed(self.sidebar_page_objects.fungibles_button()):
            self.sidebar_page_objects.click_fungibles_button()
