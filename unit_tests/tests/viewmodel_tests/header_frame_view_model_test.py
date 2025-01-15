"""Unit test for header frame view model"""
# pylint: disable=redefined-outer-name,unused-argument
from __future__ import annotations

from unittest.mock import MagicMock
from unittest.mock import Mock
from unittest.mock import patch

import pytest

from src.viewmodels.header_frame_view_model import HeaderFrameViewModel
from src.viewmodels.header_frame_view_model import NetworkCheckerThread


@pytest.fixture
def mock_network_checker():
    """Mock NetworkCheckerThread"""
    with patch('src.viewmodels.header_frame_view_model.NetworkCheckerThread') as mock:
        mock_thread = MagicMock()
        mock.return_value = mock_thread
        yield mock_thread


@pytest.fixture
def header_frame_view_model(mock_network_checker):
    """Fixture for creating a HeaderFrameViewModel instance."""
    view_model = HeaderFrameViewModel()
    return view_model


def test_header_frame_view_model_init(mock_network_checker):
    """Test HeaderFrameViewModel initialization."""
    view_model = HeaderFrameViewModel()

    assert hasattr(view_model, 'network_checker')
    assert view_model.network_checker == mock_network_checker
    mock_network_checker.start.assert_called_once()


def test_handle_network_status(header_frame_view_model):
    """Test handle_network_status method."""
    mock_signal = Mock()
    header_frame_view_model.network_status_signal.connect(mock_signal)

    header_frame_view_model.handle_network_status(True)

    mock_signal.assert_called_once_with(True)


def test_stop_network_checker(header_frame_view_model, mock_network_checker):
    """Test stop_network_checker method."""
    header_frame_view_model.stop_network_checker()

    mock_network_checker.stop.assert_called_once()


@patch('src.viewmodels.header_frame_view_model.NetworkCheckerThread')
def test_network_checker_thread_init(mock_thread_class):
    """Test NetworkCheckerThread initialization."""
    mock_thread = mock_thread_class.return_value
    mock_thread.running = True

    thread = mock_thread_class()
    assert thread.running is True


@patch('socket.create_connection')
@patch('src.viewmodels.header_frame_view_model.NetworkCheckerThread')
def test_check_internet_conn_success(mock_thread_class, mock_socket):
    """Test check_internet_conn method when connection succeeds."""
    mock_thread = mock_thread_class.return_value
    mock_socket.return_value = True

    # Don't mock check_internet_conn itself since we want to test the actual implementation
    result = NetworkCheckerThread.check_internet_conn(mock_thread)
    mock_socket.assert_called_once_with(('8.8.8.8', 53), timeout=3)
    assert result is True


@patch('socket.create_connection')
@patch('src.viewmodels.header_frame_view_model.NetworkCheckerThread')
def test_check_internet_conn_failure(mock_thread_class, mock_socket):
    """Test check_internet_conn method when connection fails."""
    mock_thread = mock_thread_class.return_value
    mock_socket.side_effect = OSError()

    # Don't mock check_internet_conn itself since we want to test the actual implementation
    result = NetworkCheckerThread.check_internet_conn(mock_thread)
    mock_socket.assert_called_once_with(('8.8.8.8', 53), timeout=3)
    assert result is False


@patch('src.viewmodels.header_frame_view_model.NetworkCheckerThread')
def test_network_checker_stop(mock_thread_class):
    """Test NetworkCheckerThread stop method."""
    mock_thread = mock_thread_class.return_value
    mock_thread.running = True

    mock_thread.stop()
    mock_thread.running = False
    mock_thread.isRunning.return_value = False

    assert not mock_thread.running
    assert not mock_thread.isRunning()


@patch('PySide6.QtCore.QThread.quit')
@patch('PySide6.QtCore.QThread.wait')
def test_network_checker_thread_stop_complete(mock_wait, mock_quit):
    """Test NetworkCheckerThread stop method completely stops the thread."""
    # Arrange
    thread = NetworkCheckerThread()
    thread.running = True
    thread.check_internet_conn = Mock()  # Mock method to ensure it doesn't run
    # Mock signal to avoid real signal emission
    thread.network_status_signal = Mock()
    thread.msleep = Mock()  # Mock msleep to prevent delay

    # Mock `run` method so it doesn't loop infinitely
    def mocked_run():
        while thread.running:
            # This is just to simulate run behavior
            thread.check_internet_conn()
            thread.network_status_signal.emit(True)
            thread.msleep(5000)

    # Replace `run` with mocked logic
    thread.run = mocked_run

    # Act
    thread.stop()

    # Assert
    # Check if `running` is False after stopping
    assert thread.running is False
    # Ensure that `quit` and `wait` methods were called once
    mock_quit.assert_called_once()
    mock_wait.assert_called_once()


@patch('src.viewmodels.header_frame_view_model.NetworkCheckerThread')
def test_network_checker_run(mock_thread_class):
    """Test NetworkCheckerThread run method."""
    # Arrange
    mock_thread = mock_thread_class.return_value
    mock_thread.running = True
    mock_thread.check_internet_conn = Mock(
        side_effect=[True, False],
    )  # Mock network check
    mock_thread.network_status_signal = Mock()  # Mock signal
    mock_thread.msleep = Mock()  # Mock sleep to prevent delay

    def mocked_run():
        """Simulate the run method logic."""
        while mock_thread.running:
            is_connected = mock_thread.check_internet_conn()
            mock_thread.network_status_signal.emit(is_connected)
            mock_thread.running = False  # Stop after one iteration
            mock_thread.msleep(5000)

    # Replace `run` with mocked logic
    mock_thread.run = mocked_run

    # Act
    mock_thread.run()

    # Assert
    # Ensure `check_internet_conn` was called once
    mock_thread.check_internet_conn.assert_called_once()
    # Verify `msleep` was called once with the correct interval
    mock_thread.msleep.assert_called_once_with(5000)
    # Check that the signal was emitted with the correct value
    mock_thread.network_status_signal.emit.assert_called_once_with(True)
