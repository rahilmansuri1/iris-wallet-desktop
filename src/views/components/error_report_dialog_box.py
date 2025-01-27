# pylint: disable=too-many-instance-attributes, too-many-statements
"""This module contains the ErrorReportDialog class which contains the UI for the error report dialog box"""
from __future__ import annotations

from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QDialogButtonBox
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QSpacerItem
from PySide6.QtWidgets import QVBoxLayout

from src.utils.common_utils import copy_text
from src.utils.common_utils import download_file
from src.utils.common_utils import zip_logger_folder
from src.utils.constant import CONTACT_EMAIL
from src.utils.constant import GITHUB_ISSUE_LINK
from src.utils.helpers import load_stylesheet
from src.utils.local_store import local_store


class ErrorReportDialog(QDialog):
    """This class represents the UI elements of the error report dialog"""

    def __init__(self):
        super().__init__()

        self.setObjectName('error_report_dialog_box')
        self.setStyleSheet(
            load_stylesheet(
                'views/qss/error_report_dialog.qss',
            ),
        )
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setObjectName('grid_layout')
        self.grid_layout.setContentsMargins(-1, -1, 33, 25)
        self.icon_label = QLabel(self)
        self.icon_label.setObjectName('icon_label')
        icon = QIcon.fromTheme('dialog-error')
        self.icon_label.setPixmap(icon.pixmap(70, 70))

        self.grid_layout.addWidget(
            self.icon_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter,
        )

        self.were_sorry_label = QLabel(self)
        self.were_sorry_label.setObjectName('were_sorry_label')
        self.were_sorry_label.setContentsMargins(0, 15, 2, 0)
        self.grid_layout.addWidget(self.were_sorry_label, 0, 1, 1, 2)

        self.help_us_label = QLabel(self)
        self.help_us_label.setObjectName('help_us_label')
        self.help_us_label.setWordWrap(True)

        self.grid_layout.addWidget(self.help_us_label, 1, 1, 1, 2)

        self.open_issue_label = QLabel(self)
        self.open_issue_label.setObjectName('open_issue_label')

        self.grid_layout.addWidget(self.open_issue_label, 2, 1, 1, 1)

        self.github_issue_label = QLabel(self)
        self.github_issue_label.setObjectName('github_issue_label')

        self.github_issue_label.setOpenExternalLinks(True)

        self.grid_layout.addWidget(self.github_issue_label, 2, 2, 1, 1)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setObjectName('vertical_layout')
        self.vertical_layout.setSpacing(0)
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setObjectName('horizontal_layout')
        self.horizontal_layout.setContentsMargins(-1, -1, 10, -1)
        self.email_us_label = QLabel(self)
        self.email_us_label.setObjectName('email_us_label')
        self.email_us_label.setMaximumSize(QSize(100, 16777215))

        self.horizontal_layout.addWidget(self.email_us_label)

        self.email_label = QLabel(self)
        self.email_label.setObjectName('email_label')
        self.email_label.setText(CONTACT_EMAIL)

        self.horizontal_layout.addWidget(
            self.email_label, Qt.AlignmentFlag.AlignHCenter,
        )

        self.copy_button = QPushButton(self)
        self.copy_button.setObjectName('copy_button')
        self.copy_button.setMaximumSize(QSize(16, 16))
        self.copy_button.setStyleSheet('background:none')
        icon = QIcon()
        icon.addFile(
            ':/assets/copy.png', QSize(),
            QIcon.Mode.Normal, QIcon.State.Off,
        )
        self.copy_button.setIcon(icon)
        self.copy_button.setFlat(True)
        self.copy_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontal_layout.addWidget(
            self.copy_button, Qt.AlignmentFlag.AlignLeft,
        )

        self.horizontal_spacer = QSpacerItem(
            20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed,
        )

        self.horizontal_layout.addItem(self.horizontal_spacer)

        self.vertical_layout.addLayout(self.horizontal_layout)

        self.no_reply_label = QLabel(self)
        self.no_reply_label.setObjectName('no_reply_label')
        self.vertical_layout.addWidget(
            self.no_reply_label, Qt.AlignmentFlag.AlignTop,
        )

        self.grid_layout.addLayout(self.vertical_layout, 3, 1, 1, 2)

        self.vertical_spacer = QSpacerItem(
            20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum,
        )

        self.grid_layout.addItem(self.vertical_spacer, 4, 1)

        self.thank_you_label = QLabel(self)
        self.thank_you_label.setObjectName('thank_you_label')

        self.grid_layout.addWidget(self.thank_you_label, 5, 1, 1, 2)

        self.vertical_spacer_2 = QSpacerItem(
            20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum,
        )

        self.grid_layout.addItem(self.vertical_spacer_2, 6, 1)
        self.button_box = QDialogButtonBox(self)
        self.button_box.setObjectName('buttonBox')
        self.button_box.setOrientation(Qt.Orientation.Horizontal)

        self.download_debug_logs = QPushButton(self)
        self.download_debug_logs.setObjectName('download_debug_logs')
        self.download_debug_logs.setMinimumSize(QSize(120, 40))
        self.download_debug_logs.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor),
        )
        self.button_box.addButton(
            self.download_debug_logs, QDialogButtonBox.ActionRole,
        )

        self.grid_layout.addWidget(self.button_box, 7, 1, 1, 2)

        self.retranslate_ui()
        self.setup_ui()

    def retranslate_ui(self):
        """translations for the error report dialog"""
        self.setWindowTitle(
            QCoreApplication.translate(
                'iris_wallet_desktop', 'error_report', None,
            ),
        )
        self.were_sorry_label.setText(
            QCoreApplication.translate(
                'iris_wallet_desktop', 'something_went_wrong_mb', None,
            ),
        )
        self.help_us_label.setText(
            QCoreApplication.translate(
                'iris_wallet_desktop', 'please_help_us', None,
            ),
        )
        self.open_issue_label.setText(
            QCoreApplication.translate(
                'iris_wallet_desktop', 'open_an_issue', None,
            ),
        )
        self.github_issue_label.setText(
            f"""<a href="{GITHUB_ISSUE_LINK}" style="text-decoration:underline;color:green;">
                    {
                QCoreApplication.translate(
                    "iris_wallet_desktop", "github_issue_label", None
                )
            }</a>
                    """,
        )
        self.email_us_label.setText(
            QCoreApplication.translate(
                'iris_wallet_desktop', 'email_us_at', None,
            ),
        )
        self.no_reply_label.setText(f"({
            QCoreApplication.translate(
                "iris_wallet_desktop", "do_not_expect_reply", None
            )
        })")
        self.thank_you_label.setText(
            QCoreApplication.translate(
                'iris_wallet_desktop', 'thank_you_for_your_support', None,
            ),
        )
        self.download_debug_logs.setText(
            QCoreApplication.translate(
                'iris_wallet_desktop', 'download_debug_log', None,
            ),
        )

    def setup_ui(self):
        """Ui connections for error report dialog"""
        self.copy_button.clicked.connect(lambda: copy_text(self.email_label))
        self.download_debug_logs.clicked.connect(
            self.on_click_download_debug_log,
        )

    def on_click_download_debug_log(self):
        """This method opens the file dialog box and saves the debug logs to the selected path"""

        path = local_store.get_path()
        zip_filename, output_dir = zip_logger_folder(path)

        save_path, _ = QFileDialog.getSaveFileName(
            self, 'Save logs File', zip_filename, 'Zip Files (*.zip)',
        )

        if save_path:
            download_file(save_path, output_dir)
