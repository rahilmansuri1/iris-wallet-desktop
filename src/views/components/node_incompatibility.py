# pylint: disable=too-few-public-methods
"""Module for displaying a dialog that alerts the user about node incompatibility issues."""
from __future__ import annotations

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QMessageBox

from src.utils.constant import IRIS_WALLET_TRANSLATIONS_CONTEXT


class NodeIncompatibilityDialog:
    """Handles the display of a warning dialog when the RGB Lightning Node is incompatible.

    The dialog provides two options:
    - **Delete App Data:** Resets the wallet by deleting stored data.
    - **Quit App:** Closes the application.

    The dialog remains open until the user makes a selection.
    """

    def __init__(self):
        """Initializes and displays the node incompatibility dialog.

        Features:
        - A warning icon indicating a critical issue.
        - A message explaining the incompatibility and suggesting solutions.
        - A 'Delete App Data' button for resetting the wallet.
        - A 'Quit App' button to close the application.
        - The 'Delete App Data' button is set as the default option.
        """
        super().__init__()

        self.confirm_delete_button = None
        self.confirmation_dialog = None
        self.cancel = None

        self.node_incompatibility_dialog = QMessageBox()

        self.node_incompatibility_dialog.setIcon(QMessageBox.Icon.Warning)
        self.node_incompatibility_dialog.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'node_incompatibility_dialog_desc', None,
            ),
        )
        self.delete_app_data_button = self.node_incompatibility_dialog.addButton(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'delete_app_data', None,
            ),
            QMessageBox.AcceptRole,
        )
        self.close_button = self.node_incompatibility_dialog.addButton(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'crash_dialog_close_app', None,
            ),
            QMessageBox.RejectRole,
        )
        self.node_incompatibility_dialog.setDefaultButton(self.close_button)

        self.node_incompatibility_dialog.exec()

    def show_confirmation_dialog(self):
        """Displays a confirmation dialog before deleting app data.

        This dialog warns the user about the consequences of data deletion and
        provides two options:
        - **Delete Data:** Confirms the deletion of stored wallet data.
        - **Cancel:** Aborts the deletion process.
        """
        self.confirmation_dialog = QMessageBox()
        self.confirmation_dialog.setIcon(QMessageBox.Icon.Critical)
        self.confirmation_dialog.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'confirm_app_data_deletion', None,
            ),
        )
        self.confirm_delete_button = self.confirmation_dialog.addButton(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'delete_app_data', None,
            ), QMessageBox.AcceptRole,
        )
        self.cancel = self.confirmation_dialog.addButton(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'cancel', None,
            ), QMessageBox.RejectRole,
        )

        self.confirmation_dialog.exec()
