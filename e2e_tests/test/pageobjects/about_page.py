"""This module contains the page object for About page"""
from __future__ import annotations

from accessible_constant import ANNOUNCE_ADDRESS_ACCESSIBLE_DESCRIPTION
from accessible_constant import ANNOUNCE_ALIAS_ACCESSIBLE_DESCRIPTION
from accessible_constant import INDEXER_URL_ACCESSIBLE_DESCRIPTION
from accessible_constant import LN_PEER_LISTENING_PORT_COPY_BUTTON
from accessible_constant import NODE_PUBKEY_COPY_BUTTON
from accessible_constant import RGB_PROXY_URL_ACCESSIBLE_DESCRIPTION
from e2e_tests.test.utilities.base_operation import BaseOperations


class AboutPageObjects(BaseOperations):
    """Class for about page object"""

    def __init__(self, application):
        super().__init__(application)

        self.announce_address_label = lambda: self.perform_action_on_element(
            role_name='label', description=ANNOUNCE_ADDRESS_ACCESSIBLE_DESCRIPTION,
        )
        self.announce_alias_label = lambda: self.perform_action_on_element(
            role_name='label', description=ANNOUNCE_ALIAS_ACCESSIBLE_DESCRIPTION,
        )
        self.node_pubkey_copy_button = lambda: self.perform_action_on_element(
            role_name='push button', name=NODE_PUBKEY_COPY_BUTTON,
        )
        self.ln_peer_listening_port_copy_button = lambda: self.perform_action_on_element(
            role_name='push button', name=LN_PEER_LISTENING_PORT_COPY_BUTTON,
        )
        self.indexer_url_label = lambda: self.perform_action_on_element(
            role_name='label', description=INDEXER_URL_ACCESSIBLE_DESCRIPTION,
        )
        self.rgb_proxy_url = lambda: self.perform_action_on_element(
            role_name='label', description=RGB_PROXY_URL_ACCESSIBLE_DESCRIPTION,
        )

    def get_announce_address(self):
        """Returns the announce address"""
        return self.do_get_text(self.announce_address_label()) if self.do_is_displayed(self.announce_address_label()) else None

    def get_announce_alias(self):
        """Returns the announce alias"""
        return self.do_get_text(self.announce_alias_label()) if self.do_is_displayed(self.announce_alias_label()) else None

    def get_indexer_url(self):
        """Returns the indexer url"""
        return self.do_get_text(self.indexer_url_label()) if self.do_is_displayed(self.indexer_url_label()) else None

    def get_rgb_proxy_url(self):
        """Returns the rgb proxy url"""
        return self.do_get_text(self.rgb_proxy_url()) if self.do_is_displayed(self.rgb_proxy_url()) else None

    def click_node_pubkey_button(self):
        """Clicks the node pubkey copy button"""
        return self.do_click(self.node_pubkey_copy_button()) if self.do_is_displayed(self.node_pubkey_copy_button()) else None

    def click_ln_peer_listening_port_copy_button(self):
        """Clicks the ln peer listening port copy button"""
        return self.do_click(self.ln_peer_listening_port_copy_button()) if self.do_is_displayed(self.ln_peer_listening_port_copy_button()) else None
