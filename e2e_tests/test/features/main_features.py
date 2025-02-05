# pylint: disable=too-few-public-methods
"""
Main Features Module.
"""
from __future__ import annotations

from e2e_tests.test.features.create_channel import CreateChannel
from e2e_tests.test.features.issue_rgb20 import IssueRgb20
from e2e_tests.test.features.issue_rgb25 import IssueRgb25
from e2e_tests.test.features.receive import ReceiveOperation
from e2e_tests.test.features.send import SendOperation
from e2e_tests.test.features.wallet import Wallet


class MainFeatures():
    """
    Main Features Class.
    """

    def __init__(self, application):
        """
        Initializes the MainFeatures class.
        """
        self.application = application

        self.wallet_features = Wallet(self.application)

        self.issue_rgb20_features = IssueRgb20(self.application)

        self.issue_rgb25_features = IssueRgb25(self.application)

        self.receive_features = ReceiveOperation(self.application)

        self.send_features = SendOperation(self.application)

        self.create_channel_features = CreateChannel(self.application)
