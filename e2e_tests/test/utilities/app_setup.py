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

import psutil  # Added for tracking child processes
import pytest
from dogtail.tree import root

from accessible_constant import FIRST_APPLICATION
from accessible_constant import SECOND_APPLICATION
from e2e_tests.test.features.main_features import MainFeatures
from e2e_tests.test.pageobjects.main_page_objects import MainPageObjects
from e2e_tests.test.utilities.base_operation import BaseOperations
from e2e_tests.test.utilities.reset_app import delete_app_data


class TestEnvironment:
    """
    A class representing the test environment for the Iris Wallet application.
    """

    def __init__(self, multi_instance=True,  skip_reset=False):
        """
        Initializes the test environment.

        Args:
        multi_instance (bool): If True, launches both applications. Otherwise, only launches one.
        """
        self.multi_instance = multi_instance
        self.skip_reset = skip_reset

        # Initialize attributes
        self.first_process = None
        self.second_process = None
        self.first_page_features = None
        self.second_page_features = None
        self.first_page_objects = None
        self.second_page_objects = None
        self.first_operations = None
        self.second_operations = None

        # Reset app data before starting
        if not self.skip_reset:
            self.reset_app_data()

        # Launch applications
        self.launch_applications()

        # Initialize first application
        self.first_application = root.child(
            roleName='frame', name=FIRST_APPLICATION,
        )
        self.first_page_features = MainFeatures(self.first_application)
        self.first_page_objects = MainPageObjects(self.first_application)
        self.first_operations = BaseOperations(self.first_application)

        # Initialize second application only if multi_instance is enabled
        if self.multi_instance:
            self.second_application = root.child(
                roleName='frame', name=SECOND_APPLICATION,
            )
            self.second_page_features = MainFeatures(self.second_application)
            self.second_page_objects = MainPageObjects(self.second_application)
            self.second_operations = BaseOperations(self.second_application)

    def reset_app_data(self):
        """Resets the app data by deleting relevant directories."""
        delete_app_data(
            '/home/dhimant/snap/code/181/.local/share/rgb/iriswallet',
        )
        if self.multi_instance:
            delete_app_data(
                '/home/dhimant/snap/code/181/.local/share/rgb_app_1/iriswallet_app_1',
            )

    def launch_applications(self):
        """Launches the required Iris Wallet applications and maximizes the windows."""
        self.first_process = subprocess.Popen(
            ['e2e_tests/applications/iriswallet-0.1.0-x86_64.AppImage'],
        )
        self.wait_for_application(FIRST_APPLICATION)

        # Maximize first application window
        window_name = FIRST_APPLICATION
        subprocess.run(
            [
                'wmctrl', '-r', window_name, '-b',
                'add,maximized_vert,maximized_horz',
            ], check=True,
        )

        if self.multi_instance:
            self.second_process = subprocess.Popen(
                ['e2e_tests/applications/iriswallet_app_1-0.1.0-x86_64.AppImage'],
            )
            self.wait_for_application(SECOND_APPLICATION)

            # Maximize second application window
            window_name = SECOND_APPLICATION
            subprocess.run(
                [
                    'wmctrl', '-r', window_name, '-b',
                    'add,maximized_vert,maximized_horz',
                ], check=True,
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
        """Gracefully terminates a process and its children, handling the exit confirmation dialog."""
        if not process:
            return

        pid = process.pid
        if not pid:
            return

        # Get all child processes
        child_pids = self.get_child_pids(pid)

        os.kill(pid, signal.SIGKILL)  # Graceful shutdown
        for child_pid in child_pids:
            os.kill(child_pid, signal.SIGKILL)

    def terminate(self):
        """Cleans up the test environment by shutting down applications."""
        self.terminate_process(self.first_process)
        if self.multi_instance:
            self.terminate_process(self.second_process)


@pytest.fixture(scope='module')
def test_environment(request):
    """
    A fixture that sets up and tears down the test environment.

    Use `request.param` to determine if multi-instance should be enabled.
    """
    multi_instance = getattr(request, 'param', True)
    skip_reset = request.node.get_closest_marker('skip_reset') is not None
    env = TestEnvironment(multi_instance=multi_instance, skip_reset=skip_reset)
    yield env
    env.terminate()


@pytest.fixture
def wallets_and_operations(test_environment):
    """
    A fixture that initializes the wallets and operations objects.
    """
    first_page_features: MainFeatures = test_environment.first_page_features
    second_page_features: MainFeatures = test_environment.second_page_features if test_environment.multi_instance else None
    first_page_objects: MainPageObjects = test_environment.first_page_objects
    second_page_objects: MainPageObjects = test_environment.second_page_objects if test_environment.multi_instance else None
    first_operations: BaseOperations = test_environment.first_operations
    second_operations: BaseOperations = test_environment.second_operations if test_environment.multi_instance else None

    return first_page_features, second_page_features, first_page_objects, second_page_objects, first_operations, second_operations
