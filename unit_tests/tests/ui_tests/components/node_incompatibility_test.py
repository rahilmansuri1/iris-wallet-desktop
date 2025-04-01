"""Unit tests for node incompatibility dialog box"""
from __future__ import annotations

from unittest.mock import MagicMock

from PySide6.QtWidgets import QMessageBox

from src.views.components.node_incompatibility import NodeIncompatibilityDialog


def test_node_incompatibility_dialog(monkeypatch):
    """Tests the initialization and display of the node incompatibility dialog."""

    mock_exec = MagicMock()
    monkeypatch.setattr(QMessageBox, 'exec', mock_exec)

    dialog = NodeIncompatibilityDialog()

    assert dialog.node_incompatibility_dialog.icon() == QMessageBox.Icon.Warning
    assert dialog.node_incompatibility_dialog.text() is not None
    assert dialog.delete_app_data_button is not None
    assert dialog.close_button is not None
    assert dialog.node_incompatibility_dialog.defaultButton() == dialog.close_button
    mock_exec.assert_called_once()


def test_show_confirmation_dialog(monkeypatch):
    """Tests the confirmation dialog for app data deletion."""

    mock_exec = MagicMock()
    monkeypatch.setattr(QMessageBox, 'exec', mock_exec)

    dialog = NodeIncompatibilityDialog()
    dialog.show_confirmation_dialog()

    assert dialog.confirmation_dialog.icon() == QMessageBox.Icon.Critical
    assert dialog.confirmation_dialog.text() is not None
    assert dialog.confirm_delete_button is not None
    assert dialog.cancel is not None
    mock_exec.assert_called()
