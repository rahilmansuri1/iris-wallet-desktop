"""View model to handle network connectivity check or other logic for header"""
from __future__ import annotations

import socket

from PySide6.QtCore import QObject
from PySide6.QtCore import QThread
from PySide6.QtCore import Signal

from src.utils.constant import PING_DNS_ADDRESS_FOR_NETWORK_CHECK
from src.utils.constant import PING_DNS_SERVER_CALL_INTERVAL


class NetworkCheckerThread(QThread):
    """View model to handle network connectivity"""
    network_status_signal = Signal(bool)
    _instance = None

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        """Run the network checking loop."""
        while self.running:
            is_connected = self.check_internet_conn()
            self.network_status_signal.emit(is_connected)
            # Wait 5 seconds before the next check
            self.msleep(PING_DNS_SERVER_CALL_INTERVAL)

    def check_internet_conn(self):
        """Check internet connection by making a request to the specified URL."""
        try:
            # Attempt to resolve the hostname of Google to test internet
            socket.create_connection(
                (PING_DNS_ADDRESS_FOR_NETWORK_CHECK, 53), timeout=3,
            )
            return True
        except OSError:
            return False

    def stop(self):
        """Stop the thread."""
        self.running = False
        self.quit()
        self.wait()


class HeaderFrameViewModel(QObject):
    """Handle network connectivity"""
    network_status_signal = Signal(bool)

    def __init__(self):
        super().__init__()  # Call the parent constructor
        self.network_checker = NetworkCheckerThread()
        self.network_checker.network_status_signal.connect(
            self.handle_network_status,
        )
        self.network_checker.start()

    def handle_network_status(self, is_connected):
        """Handle the network status change."""
        self.network_status_signal.emit(is_connected)

    def stop_network_checker(self):
        """Stop the network checker when no longer needed."""
        self.network_checker.stop()
