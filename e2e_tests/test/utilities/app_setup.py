# pylint: disable=too-many-instance-attributes, redefined-outer-name, consider-using-with
"""
This module provides a test environment for the Iris Wallet application.
It includes classes and fixtures for setting up and tearing down the test environment.
"""
from __future__ import annotations

import os
import signal
import subprocess
import time

import psutil
import pytest
from dogtail.tree import root

from accessible_constant import FIRST_APPLICATION
from accessible_constant import SECOND_APPLICATION
from e2e_tests.test.features.main_features import MainFeatures
from e2e_tests.test.pageobjects.main_page_objects import MainPageObjects
from e2e_tests.test.utilities.base_operation import BaseOperations
from e2e_tests.test.utilities.model import WalletTestSetup
from e2e_tests.test.utilities.reset_app import delete_app_data
from e2e_tests.test.utilities.translation_utils import TranslationManager
from src.version import __version__


class TestEnvironment:
    """
    A class representing the test environment for the Iris Wallet application.
    """

    def __init__(self, wallet_mode, multi_instance=True, skip_reset=False):
        """
        Initializes the test environment.

        Args:
            wallet_mode (str): Determines whether to use "embedded" or "connect" wallet.
            multi_instance (bool): If True, launches both applications. Otherwise, only launches one.
            skip_reset (bool): If True, skips resetting the application data.
        """
        self.multi_instance = multi_instance
        self.skip_reset = skip_reset
        self.wallet_mode = wallet_mode

        # Initialize process attributes
        self.first_process = None
        self.second_process = None
        self.rgb_processes = []

        # Reset app data before starting
        if not self.skip_reset:
            self.reset_app_data()

        # Start applications based on wallet mode
        if self.wallet_mode == 'connect':
            self.start_rgb_lightning_nodes()

        self.launch_applications()

        # Initialize first application
        self.first_application = root.child(
            roleName='frame', name=FIRST_APPLICATION,
        )
        self.first_page_features = MainFeatures(self.first_application)
        self.first_page_objects = MainPageObjects(self.first_application)
        self.first_page_operations = BaseOperations(self.first_application)

        # Initialize second application if multi-instance is enabled
        if self.multi_instance:
            self.second_application = root.child(
                roleName='frame', name=SECOND_APPLICATION,
            )
            self.second_page_features = MainFeatures(self.second_application)
            self.second_page_objects = MainPageObjects(self.second_application)
            self.second_page_operations = BaseOperations(
                self.second_application,
            )

    def reset_app_data(self):
        """Resets the app data by deleting relevant directories."""
        delete_app_data('/home/zoro/.local/share/rgb/iriswallet')
        delete_app_data('dataldk0')
        if self.multi_instance:
            delete_app_data(
                '/home/zoro/.local/share/rgb_app_1/iriswallet_app_1',
            )
            delete_app_data('dataldk1')

    def start_rgb_lightning_nodes(self):
        """Starts two RGB Lightning Nodes when wallet mode is 'connect'."""
        self.rgb_processes.append(self.start_rgb_node('dataldk0', 3001, 9735))
        if self.multi_instance:
            self.rgb_processes.append(
                self.start_rgb_node('dataldk1', 3002, 9736),
            )

    def start_rgb_node(self, data_dir, daemon_port, peer_port):
        """
        Starts an RGB Lightning Node.

        Args:
            data_dir (str): Directory for node data.
            daemon_port (int): Port for daemon listening.
            peer_port (int): Port for LDK peer listening.

        Returns:
            subprocess.Popen: The process object.
        """
        command = [
            'rgb-lightning-node',
            data_dir,
            '--daemon-listening-port',
            str(daemon_port),
            '--ldk-peer-listening-port',
            str(peer_port),
            '--network',
            'regtest',
        ]
        process = subprocess.Popen(command)
        return process

    def launch_applications(self):
        """Launches the required Iris Wallet applications and maximizes the windows."""
        self.first_process = subprocess.Popen(
            [f"e2e_tests/applications/iriswallet-{
                __version__
            }-x86_64.AppImage"],
        )
        self.wait_for_application(FIRST_APPLICATION)

        # Maximize first application window
        subprocess.run(
            [
                'wmctrl', '-r', FIRST_APPLICATION, '-b',
                'add,maximized_vert,maximized_horz',
            ],
            check=True,
        )

        if self.multi_instance:
            self.second_process = subprocess.Popen(
                [f"e2e_tests/applications/iriswallet_app_1-{
                    __version__
                }-x86_64.AppImage"],
            )
            self.wait_for_application(SECOND_APPLICATION)

            # Maximize second application window
            subprocess.run(
                [
                    'wmctrl', '-r', SECOND_APPLICATION, '-b',
                    'add,maximized_vert,maximized_horz',
                ],
                check=True,
            )

    def wait_for_application(self, app_name, timeout=10):
        """Waits for an application to be fully loaded dynamically."""
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                if root.child(roleName='frame', name=app_name):
                    return True
            except Exception:
                pass
            time.sleep(0.5)  # Avoid excessive CPU usage
        raise TimeoutError(
            f"""Application '{app_name}' failed to start within {
                timeout
            } seconds""",
        )

    def get_child_pids(self, parent_pid):
        """Returns a list of child process PIDs for a given parent process."""
        try:
            parent = psutil.Process(parent_pid)
            return [child.pid for child in parent.children(recursive=True)]
        except psutil.NoSuchProcess:
            return []

    def terminate_process(self, process):
        """Gracefully terminates a process and its children."""
        if not process:
            return

        pid = process.pid
        if not pid:
            return

        # Get all child processes
        child_pids = self.get_child_pids(pid)

        os.kill(pid, signal.SIGKILL)  # Force shutdown
        for child_pid in child_pids:
            os.kill(child_pid, signal.SIGKILL)

    def terminate(self):
        """Cleans up the test environment by shutting down applications and RGB nodes."""
        self.terminate_process(self.first_process)
        if self.multi_instance:
            self.terminate_process(self.second_process)

        # Terminate RGB Lightning Nodes
        for process in self.rgb_processes:
            self.terminate_process(process)


@pytest.fixture(scope='module')
def test_environment(request):
    """
    A fixture that sets up and tears down the test environment.

    Use `request.param` to determine if multi-instance should be enabled.
    """
    multi_instance = getattr(request, 'param', True)
    skip_reset = request.node.get_closest_marker('skip_reset') is not None
    wallet_mode = request.config.getoption(
        '--wallet-mode',
    )  # Get wallet mode from pytest

    env = TestEnvironment(
        multi_instance=multi_instance, skip_reset=skip_reset, wallet_mode=wallet_mode,
    )
    yield env
    env.terminate()


@pytest.fixture
def wallets_and_operations(test_environment) -> WalletTestSetup:
    """
    A fixture that initializes the wallets and operations objects.
    """
    return WalletTestSetup(
        first_page_features=test_environment.first_page_features,
        second_page_features=test_environment.second_page_features
        if test_environment.multi_instance
        else None,
        first_page_objects=test_environment.first_page_objects,
        second_page_objects=test_environment.second_page_objects
        if test_environment.multi_instance
        else None,
        first_page_operations=test_environment.first_page_operations,
        second_page_operations=test_environment.second_page_operations
        if test_environment.multi_instance
        else None,
        wallet_mode=test_environment.wallet_mode,
    )


@pytest.fixture(scope='session', autouse=True)
def load_qm_translation():
    """Load the .qm translation file once per test session."""
    TranslationManager.load_translation()
