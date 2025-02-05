# pylint: disable=too-many-instance-attributes, too-many-public-methods
"""This module represents the page object for the settings page"""
from __future__ import annotations

from accessible_constant import EXPIRY_TIME_COMBO_BOX
from accessible_constant import INPUT_BOX_NAME
from accessible_constant import SET_DEFAULT_EXP_TIME
from accessible_constant import SET_DEFAULT_FEE_RATE
from accessible_constant import SET_DEFAULT_MIN_EXPIRATION
from accessible_constant import SPECIFY_ANNOUNCE_ADD
from accessible_constant import SPECIFY_ANNOUNCE_ALIAS
from accessible_constant import SPECIFY_BITCOIND_HOST
from accessible_constant import SPECIFY_BITCOIND_PORT
from accessible_constant import SPECIFY_INDEXER_URL
from accessible_constant import SPECIFY_RGB_PROXY_URL
from e2e_tests.test.utilities.base_operation import BaseOperations


class SettingsPageObjects(BaseOperations):
    """Class for Settings page objects"""

    def __init__(self, application):
        """Class for the settings page object"""

        super().__init__(application)

        # Settings frames
        self.default_fee_rate_frame = lambda: self.perform_action_on_element(
            role_name='panel', name=SET_DEFAULT_FEE_RATE,
        )
        self.default_exp_time_frame = lambda: self.perform_action_on_element(
            role_name='panel', name=SET_DEFAULT_EXP_TIME,
        )
        self.set_min_confirmation_frame = lambda: self.perform_action_on_element(
            role_name='panel', name=SET_DEFAULT_MIN_EXPIRATION,
        )
        self.specify_indexer_url_frame = lambda: self.perform_action_on_element(
            role_name='panel', name=SPECIFY_INDEXER_URL,
        )
        self.specify_rgb_proxy_url_frame = lambda: self.perform_action_on_element(
            role_name='panel', name=SPECIFY_RGB_PROXY_URL,
        )
        self.specify_bitcoind_host_frame = lambda: self.perform_action_on_element(
            role_name='panel', name=SPECIFY_BITCOIND_HOST,
        )
        self.specify_bitcoind_port_frame = lambda: self.perform_action_on_element(
            role_name='panel', name=SPECIFY_BITCOIND_PORT,
        )
        self.specify_announce_address_frame = lambda: self.perform_action_on_element(
            role_name='panel', name=SPECIFY_ANNOUNCE_ADD,
        )
        self.specify_announce_alias_frame = lambda: self.perform_action_on_element(
            role_name='panel', name=SPECIFY_ANNOUNCE_ALIAS,
        )
        self.save_button = lambda: self.perform_action_on_element(
            role_name='push button', name='Save',
        )
        self.expiry_combo_box = lambda: self.perform_action_on_element(
            role_name='combo box', description=EXPIRY_TIME_COMBO_BOX,
        )
        self.hour_list_item = lambda: self.perform_action_on_element(
            role_name='list item', name='Minutes',
        )
        self.minute_list_item = lambda: self.perform_action_on_element(
            role_name='list item', name='Hour',
        )
        self.days_list_item = lambda: self.perform_action_on_element(
            role_name='list item', name='Days',
        )

        # Input Boxes in Frames
        self.default_fee_rate_input_box = lambda: self.perform_action_on_element(
            role_name='text', name=INPUT_BOX_NAME,
        )
        self.default_exp_time_input_box = lambda: self.perform_action_on_element(
            role_name='text', name=INPUT_BOX_NAME,
        )
        self.set_announce_address_input_box = lambda: self.perform_action_on_element(
            role_name='text', name=INPUT_BOX_NAME,
        )
        self.set_announce_alias_input_box = lambda: self.perform_action_on_element(
            role_name='text', name=INPUT_BOX_NAME,
        )
        self.set_indexer_url_input_box = lambda: self.perform_action_on_element(
            role_name='text', name=INPUT_BOX_NAME,
        )
        self.set_rgb_proxy_url_input_box = lambda: self.perform_action_on_element(
            role_name='text', name=INPUT_BOX_NAME,
        )
        self.set_bitcoind_host_input_box = lambda: self.perform_action_on_element(
            role_name='text', name=INPUT_BOX_NAME,
        )
        self.set_bitcoind_port_input_box = lambda: self.perform_action_on_element(
            role_name='text', name=INPUT_BOX_NAME,
        )

    # Default Fee Rate
    def click_default_fee_rate_frame(self):
        """Click on the default fee rate frame"""
        return self.do_click(self.default_fee_rate_frame()) if self.do_is_displayed(self.default_fee_rate_frame()) else None

    def clear_default_fee_rate(self):
        """Clear the text in default fee rate input box"""
        return self.do_clear_text(self.default_fee_rate_input_box()) if self.do_is_displayed(self.default_fee_rate_input_box()) else None

    def enter_new_default_fee_rate(self, value):
        """Enter a new value in the default fee rate input box

        Args:
            value: The new fee rate value to enter
        """
        return self.do_set_value(self.default_fee_rate_input_box(), value) if self.do_is_displayed(self.default_fee_rate_input_box()) else None

    # Default Expiry Time

    def click_default_exp_time_frame(self):
        """Click on the default expiry time frame"""
        return self.do_click(self.default_exp_time_frame()) if self.do_is_displayed(self.default_exp_time_frame()) else None

    def clear_default_exp_time(self):
        """Clear the text in default expiry time input box"""
        return self.do_clear_text(self.default_exp_time_input_box()) if self.do_is_displayed(self.default_exp_time_input_box()) else None

    def enter_new_default_expiry_time(self, value):
        """Enter a new value in the default expiry time input box

        Args:
            value: The new expiry time value to enter
        """
        return self.do_set_value(self.default_exp_time_input_box(), value) if self.do_is_displayed(self.default_exp_time_input_box()) else None

    # Minimum Confirmation

    def click_set_min_confirmation_frame(self):
        """Click on the set minimum confirmation frame"""
        return self.do_click(self.set_min_confirmation_frame()) if self.do_is_displayed(self.set_min_confirmation_frame()) else None

    # Indexer URL

    def click_set_indexer_url_frame(self):
        """Click on the indexer URL frame"""
        return self.do_click(self.specify_indexer_url_frame()) if self.do_is_displayed(self.specify_indexer_url_frame()) else None

    def clear_indexer_url(self):
        """Clear the text in indexer URL input box"""
        return self.do_clear_text(self.set_indexer_url_input_box()) if self.do_is_displayed(self.set_indexer_url_input_box()) else None

    def enter_new_indexer_url(self, value):
        """Enter a new value in the indexer URL input box

        Args:
            value: The new indexer URL to enter
        """
        return self.do_set_value(self.set_indexer_url_input_box(), value) if self.do_is_displayed(self.set_indexer_url_input_box()) else None

    # RGB Proxy URL
    def click_set_rgb_proxy_url_frame(self):
        """Click on the RGB proxy URL frame"""
        return self.do_click(self.specify_rgb_proxy_url_frame()) if self.do_is_displayed(self.specify_rgb_proxy_url_frame()) else None

    def clear_rgb_proxy_url_frame(self):
        """Clear the text in RGB proxy URL input box"""
        return self.do_clear_text(self.set_rgb_proxy_url_input_box()) if self.do_is_displayed(self.set_rgb_proxy_url_input_box()) else None

    def enter_new_rgb_proxy_url(self, value):
        """Enter a new value in the RGB proxy URL input box

        Args:
            value: The new RGB proxy URL to enter
        """
        return self.do_set_value(self.set_rgb_proxy_url_input_box(), value) if self.do_is_displayed(self.set_rgb_proxy_url_input_box()) else None

    # Bitcoind Host

    def click_specify_bitcoind_host_frame(self):
        """Click on the bitcoind host frame"""
        return self.do_click(self.specify_bitcoind_host_frame()) if self.do_is_displayed(self.specify_bitcoind_host_frame()) else None

    def clear_bitcoind_host(self):
        """Clear the text in bitcoind host input box"""
        return self.do_clear_text(self.set_bitcoind_host_input_box()) if self.do_is_displayed(self.set_bitcoind_host_input_box()) else None

    def enter_new_bitcoind_host(self, value):
        """Enter a new value in the bitcoind host input box

        Args:
            value: The new bitcoind host to enter
        """
        return self.do_set_value(self.set_bitcoind_host_input_box(), value) if self.do_is_displayed(self.set_bitcoind_host_input_box()) else None

    # Bitcoind Port

    def click_specify_bitcoind_port_frame(self):
        """Click on the bitcoind port frame"""
        return self.do_click(self.specify_bitcoind_port_frame()) if self.do_is_displayed(self.specify_bitcoind_port_frame()) else None

    def clear_bitcoind_port(self):
        """Clear the text in bitcoind port input box"""
        return self.do_clear_text(self.set_bitcoind_port_input_box()) if self.do_is_displayed(self.set_bitcoind_port_input_box()) else None

    def enter_new_bitcoind_port(self, value):
        """Enter a new value in the bitcoind port input box

        Args:
            value: The new bitcoind port to enter
        """
        return self.do_set_value(self.set_bitcoind_port_input_box(), value) if self.do_is_displayed(self.set_bitcoind_port_input_box()) else None

    # Announce Address

    def click_specify_announce_address_frame(self):
        """Click on the announce address frame"""
        return self.do_click(self.specify_announce_address_frame()) if self.do_is_displayed(self.specify_announce_address_frame()) else None

    def clear_announce_address(self):
        """Clear the text in announce address input box"""
        return self.do_clear_text(self.set_announce_address_input_box()) if self.do_is_displayed(self.set_announce_address_input_box()) else None

    def enter_new_announce_address(self, value):
        """Enter a new value in the announce address input box

        Args:
            value: The new announce address to enter
        """
        return self.do_set_value(self.set_announce_address_input_box(), value) if self.do_is_displayed(self.set_announce_address_input_box()) else None

    # Announce Alias

    def click_specify_announce_alias(self):
        """Click on the announce alias frame"""
        return self.do_click(self.specify_announce_alias_frame()) if self.do_is_displayed(self.specify_announce_alias_frame()) else None

    def clear_announce_alias(self):
        """Clear the text in announce alias input box"""
        return self.do_clear_text(self.set_announce_alias_input_box()) if self.do_is_displayed(self.set_announce_alias_input_box()) else None

    def enter_new_announce_alias(self, value):
        """Enter a new value in the announce alias input box

        Args:
            value: The new announce alias to enter
        """
        return self.do_set_value(self.set_announce_alias_input_box(), value) if self.do_is_displayed(self.set_announce_alias_input_box()) else None

    # Combo box

    def click_on_combo_box(self):
        """Click on the expiry time combo box"""
        return self.do_click(self.expiry_combo_box()) if self.do_is_displayed(self.expiry_combo_box()) else None

    def click_on_hour(self):
        """Click on the hour option in the combo box"""
        return self.do_click(self.hour_list_item()) if self.do_is_displayed(self.hour_list_item()) else None

    def click_on_minute(self):
        """Click on the minute option in the combo box"""
        return self.do_click(self.minute_list_item()) if self.do_is_displayed(self.minute_list_item()) else None

    def click_on_days(self):
        """Click on the days option in the combo box"""
        return self.do_click(self.days_list_item()) if self.do_is_displayed(self.days_list_item()) else None

    # Save Button

    def click_save_button(self):
        """Click on the save button to save settings"""
        return self.do_click(self.save_button()) if self.do_is_displayed(self.save_button()) else None
