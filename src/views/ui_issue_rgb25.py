# pylint: disable=too-many-instance-attributes, too-many-statements, unused-import
"""This module contains the IssueRGB25Widget class,
 which represents the UI for issuing RGB25 assets.
 """
from __future__ import annotations

import os

from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtGui import QIcon
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QSpacerItem
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

import src.resources_rc
from src.model.common_operation_model import NodeInfoResponseModel
from src.model.node_info_model import NodeInfoModel
from src.model.success_model import SuccessPageModel
from src.utils.common_utils import resize_image
from src.utils.common_utils import set_number_validator
from src.utils.common_utils import set_placeholder_value
from src.utils.constant import IRIS_WALLET_TRANSLATIONS_CONTEXT
from src.utils.helpers import load_stylesheet
from src.utils.render_timer import RenderTimer
from src.viewmodels.main_view_model import MainViewModel
from src.views.components.buttons import PrimaryButton
from src.views.components.wallet_logo_frame import WalletLogoFrame


class IssueRGB25Widget(QWidget):
    """This class represents the UI for issuing RGB25 assets."""

    def __init__(self, view_model: MainViewModel):
        """Initialize the IssueRGB25Widget class."""
        super().__init__()
        self.render_timer = RenderTimer(task_name='IssueRGB25Asset Rendering')
        self.setStyleSheet(load_stylesheet('views/qss/issue_rgb25_style.qss'))
        self._view_model: MainViewModel = view_model
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setObjectName('gridLayout')
        self.wallet_logo_frame = WalletLogoFrame()

        self.grid_layout.addWidget(self.wallet_logo_frame, 0, 0, 1, 1)

        self.vertical_spacer = QSpacerItem(
            20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding,
        )

        self.grid_layout.addItem(self.vertical_spacer, 0, 2, 1, 1)

        self.issue_rgb_25_card = QWidget(self)
        self.issue_rgb_25_card.setObjectName('issue_rgb_25_card')
        self.issue_rgb_25_card.setMinimumSize(QSize(499, 608))
        self.issue_rgb_25_card.setMaximumSize(QSize(499, 608))
        self.grid_layout_1 = QGridLayout(self.issue_rgb_25_card)
        self.grid_layout_1.setObjectName('gridLayout_26')
        self.grid_layout_1.setContentsMargins(1, -1, 1, 35)
        self.horizontal_spacer_1 = QSpacerItem(
            20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed,
        )

        self.grid_layout_1.addItem(self.horizontal_spacer_1, 6, 0)

        self.issue_rgb25_button = PrimaryButton()
        self.issue_rgb25_button.setMinimumSize(QSize(402, 40))
        self.issue_rgb25_button.setMaximumSize(QSize(402, 40))

        self.grid_layout_1.addWidget(
            self.issue_rgb25_button, 7, 0, Qt.AlignCenter,
        )

        self.header_line = QFrame(self.issue_rgb_25_card)
        self.header_line.setObjectName('line_top')

        self.header_line.setFrameShape(QFrame.Shape.HLine)
        self.header_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.grid_layout_1.addWidget(self.header_line, 1, 0, 1, 1)

        self.issue_rgb25_details_layout = QVBoxLayout()
        self.issue_rgb25_details_layout.setSpacing(12)
        self.issue_rgb25_details_layout.setObjectName('vertical_layout_6')
        self.issue_rgb25_details_layout.setContentsMargins(45, 15, 45, -1)
        self.asset_name_label = QLabel(self.issue_rgb_25_card)
        self.asset_name_label.setObjectName('asset_name_label')
        self.asset_name_label.setAutoFillBackground(False)

        self.asset_name_label.setFrameShadow(QFrame.Plain)
        self.asset_name_label.setLineWidth(1)

        self.issue_rgb25_details_layout.addWidget(self.asset_name_label)

        self.name_of_the_asset_input = QLineEdit(self.issue_rgb_25_card)
        self.name_of_the_asset_input.setObjectName('name_of_the_asset_input')
        self.name_of_the_asset_input.setMinimumSize(QSize(403, 40))
        self.name_of_the_asset_input.setMaximumSize(QSize(403, 16777215))
        self.name_of_the_asset_input.setClearButtonEnabled(True)
        self.issue_rgb25_details_layout.addWidget(self.name_of_the_asset_input)

        self.asset_description_label = QLabel(self.issue_rgb_25_card)
        self.asset_description_label.setObjectName('asset_description_label')

        self.asset_description_input = QLineEdit(self.issue_rgb_25_card)
        self.asset_description_input.setObjectName('asset_description_input')
        self.asset_description_input.setMinimumSize(QSize(403, 40))
        self.asset_description_input.setMaximumSize(QSize(403, 16777215))
        self.asset_description_input.setFrame(False)
        self.asset_description_input.setClearButtonEnabled(True)

        self.issue_rgb25_details_layout.addWidget(self.asset_description_label)

        self.issue_rgb25_details_layout.addWidget(self.asset_description_input)
        self.total_supply_label = QLabel(self.issue_rgb_25_card)
        self.total_supply_label.setObjectName('total_supply_label')

        self.issue_rgb25_details_layout.addWidget(self.total_supply_label)

        self.amount_input = QLineEdit(self.issue_rgb_25_card)
        self.amount_input.setObjectName('amount_input')
        self.amount_input.setMinimumSize(QSize(403, 40))
        self.amount_input.setMaximumSize(QSize(403, 40))
        self.amount_input.setClearButtonEnabled(True)
        set_number_validator(self.amount_input)

        self.issue_rgb25_details_layout.addWidget(self.amount_input)

        self.vertical_spacer_3 = QSpacerItem(
            20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding,
        )

        self.issue_rgb25_details_layout.addItem(self.vertical_spacer_3)

        self.form_divider_line = QFrame(self.issue_rgb_25_card)
        self.form_divider_line.setObjectName('line_bottom')
        self.form_divider_line.setMinimumSize(QSize(403, 1))
        self.form_divider_line.setMaximumSize(QSize(403, 1))

        self.form_divider_line.setFrameShape(QFrame.Shape.HLine)
        self.form_divider_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.issue_rgb25_details_layout.addWidget(
            self.form_divider_line, 0, Qt.AlignHCenter,
        )

        self.vertical_spacer_4 = QSpacerItem(
            20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding,
        )

        self.issue_rgb25_details_layout.addItem(self.vertical_spacer_4)

        self.asset_file = QLabel(self.issue_rgb_25_card)
        self.asset_file.setObjectName('asset_file')
        self.asset_file.setMinimumSize(QSize(403, 17))
        self.asset_file.setMaximumSize(QSize(403, 16777215))

        self.issue_rgb25_details_layout.addWidget(self.asset_file)

        self.upload_file = QPushButton(self.issue_rgb_25_card)
        self.upload_file.setObjectName('upload_file')
        self.upload_file.setMinimumSize(QSize(403, 40))
        self.upload_file.setMaximumSize(QSize(403, 40))
        self.upload_file.setAcceptDrops(False)
        self.upload_file.setLayoutDirection(Qt.LeftToRight)

        self.upload_file.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor),
        )
        icon = QIcon()
        icon.addFile(':/assets/upload.png', QSize(), QIcon.Normal, QIcon.Off)
        self.upload_file.setIcon(icon)

        self.issue_rgb25_details_layout.addWidget(
            self.upload_file, 0, Qt.AlignHCenter,
        )
        self.file_path = QLabel(self.issue_rgb_25_card)
        self.file_path.setObjectName('asset_ti')

        self.issue_rgb25_details_layout.addWidget(
            self.file_path, 0, Qt.AlignHCenter,
        )
        self.vertical_spacer_5 = QSpacerItem(
            20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred,
        )

        self.issue_rgb25_details_layout.addItem(self.vertical_spacer_5)

        self.grid_layout_1.addLayout(
            self.issue_rgb25_details_layout, 2, 0, 1, 1,
        )

        self.grid_layout_2 = QGridLayout()
        self.grid_layout_2.setSpacing(0)
        self.grid_layout_2.setObjectName('grid_layout_2')
        self.grid_layout_2.setContentsMargins(36, 8, 40, -1)
        self.issue_rgb_25_asset_title_label = QLabel(self.issue_rgb_25_card)
        self.issue_rgb_25_asset_title_label.setObjectName(
            'issue_rgb_25_asset_title_label',
        )

        self.grid_layout_2.addWidget(
            self.issue_rgb_25_asset_title_label, 0, 0, 1, 1,
        )

        self.rgb_25_close_btn = QPushButton(self.issue_rgb_25_card)
        self.rgb_25_close_btn.setObjectName('rgb_25_close_btn')
        self.rgb_25_close_btn.setMinimumSize(QSize(24, 24))
        self.rgb_25_close_btn.setMaximumSize(QSize(50, 65))
        self.rgb_25_close_btn.setAutoFillBackground(False)

        icon1 = QIcon()
        icon1.addFile(
            ':/assets/x_circle.png',
            QSize(), QIcon.Normal, QIcon.Off,
        )
        self.rgb_25_close_btn.setIcon(icon1)
        self.rgb_25_close_btn.setIconSize(QSize(24, 24))
        self.rgb_25_close_btn.setCheckable(False)
        self.rgb_25_close_btn.setChecked(False)
        self.rgb_25_close_btn.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor),
        )

        self.grid_layout_2.addWidget(self.rgb_25_close_btn, 0, 1, 1, 1)

        self.grid_layout_1.addLayout(self.grid_layout_2, 0, 0, 1, 1)

        self.vertical_spacer_6 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding,
        )

        self.grid_layout_1.addItem(self.vertical_spacer_6, 5, 0, 1, 1)

        self.vertical_spacer_7 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding,
        )

        self.grid_layout_1.addItem(self.vertical_spacer_7, 7, 0, 1, 1)

        self.footer_line = QFrame(self.issue_rgb_25_card)
        self.footer_line.setObjectName('line_6')
        self.footer_line.setMinimumSize(QSize(498, 1))

        self.footer_line.setFrameShape(QFrame.Shape.HLine)
        self.footer_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.grid_layout_1.addWidget(self.footer_line, 3, 0, 1, 1)

        self.vertical_spacer_8 = QSpacerItem(
            20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred,
        )

        self.grid_layout_1.addItem(self.vertical_spacer_8, 4, 0, 1, 1)

        self.grid_layout.addWidget(self.issue_rgb_25_card, 1, 1, 2, 2)

        self.horizontal_spacer_2 = QSpacerItem(
            301, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum,
        )

        self.grid_layout.addItem(self.horizontal_spacer_2, 1, 3, 1, 1)

        self.horizontal_spacer = QSpacerItem(
            301, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum,
        )

        self.grid_layout.addItem(self.horizontal_spacer, 2, 0, 1, 1)

        self.vertical_spacer_2 = QSpacerItem(
            20, 99, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding,
        )

        self.grid_layout.addItem(self.vertical_spacer_2, 3, 1, 1, 1)
        self.issue_rgb25_button.setDisabled(True)
        self.retranslate_ui()
        self.setup_ui_connections()

    def retranslate_ui(self):
        """Retranslate the UI elements."""
        self.issue_rgb25_button.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'issue_asset', None,
            ),
        )
        self.asset_name_label.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'asset_name', None,
            ),
        )
        self.asset_description_input.setPlaceholderText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'description_of_the_asset', None,
            ),
        )
        self.asset_description_label.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'asset_description', None,
            ),
        )
        self.name_of_the_asset_input.setPlaceholderText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'name_of_the_asset', None,
            ),
        )
        self.total_supply_label.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'total_supply', None,
            ),
        )
        self.amount_input.setPlaceholderText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'amount_to_issue', None,
            ),
        )
        self.asset_file.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'asset_files', None,
            ),
        )
        self.upload_file.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'upload_file', None,
            ),
        )
        self.issue_rgb_25_asset_title_label.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'issue_new_rgb25_asset', None,
            ),
        )

    def setup_ui_connections(self):
        """Set up connections for UI elements."""
        self.rgb_25_close_btn.clicked.connect(
            self.on_close,
        )
        self.issue_rgb25_button.clicked.connect(self.on_issue_rgb25)
        self.upload_file.clicked.connect(self.on_upload_asset_file)
        self._view_model.issue_rgb25_asset_view_model.is_loading.connect(
            self.update_loading_state,
        )
        self._view_model.issue_rgb25_asset_view_model.file_upload_message.connect(
            self.show_file_preview,
        )
        self.amount_input.textChanged.connect(self.handle_button_enabled)
        self.asset_description_input.textChanged.connect(
            self.handle_button_enabled,
        )
        self.name_of_the_asset_input.textChanged.connect(
            self.handle_button_enabled,
        )
        self._view_model.issue_rgb25_asset_view_model.success_page_message.connect(
            self.show_asset_issued,
        )
        self.amount_input.textChanged.connect(
            lambda: set_placeholder_value(self.amount_input),
        )

    def show_file_preview(self, file_upload_message):
        """Preview the uploaded image"""
        node_info = NodeInfoModel()
        get_max_file_size: NodeInfoResponseModel = node_info.node_info
        max_file_size = get_max_file_size.max_media_upload_size_mb * 1024 * 1024
        file_size = os.path.getsize(file_upload_message)
        if file_size > max_file_size:
            validation_text = QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'image_validation', None,
            ).format(get_max_file_size.max_media_upload_size_mb)
            self.file_path.setText(validation_text)
            self.issue_rgb25_button.setDisabled(True)
            self.issue_rgb_25_card.setMaximumSize(QSize(499, 608))
        else:
            self.file_path.setText(file_upload_message)
            self.issue_rgb_25_card.setMaximumSize(QSize(499, 808))
            pixmap = resize_image(file_upload_message, 242, 242)
            self.file_path.setPixmap(
                QPixmap(pixmap),
            )
            self.upload_file.setText(
                QCoreApplication.translate(
                    IRIS_WALLET_TRANSLATIONS_CONTEXT, 'change_uploaded_file', 'CHANGE UPLOADED FILE',
                ),
            )
            self.issue_rgb25_button.setDisabled(False)

    def on_issue_rgb25(self):
        """Issue rgb25 while issue rgb25 button clicked"""
        asset_description = self.asset_description_input.text()
        asset_name = self.name_of_the_asset_input.text()
        total_supply = self.amount_input.text()
        self._view_model.issue_rgb25_asset_view_model.issue_rgb25_asset(
            asset_description, asset_name, total_supply,
        )

    def on_upload_asset_file(self):
        """This method handled upload asset file operation."""
        self._view_model.issue_rgb25_asset_view_model.open_file_dialog()

    def on_close(self):
        """Navigate to the collectibles page."""
        self._view_model.page_navigation.collectibles_asset_page()

    def handle_button_enabled(self):
        """Updates the enabled state of the send button."""
        if (self.amount_input.text() and self.asset_description_input.text() and self.name_of_the_asset_input.text() and self.amount_input.text() != '0'):
            self.issue_rgb25_button.setDisabled(False)
        else:
            self.issue_rgb25_button.setDisabled(True)

    def update_loading_state(self, is_loading: bool):
        """
        Updates the loading state of the proceed_wallet_password object.

        This method prints the loading state and starts or stops the loading animation
        of the proceed_wallet_password object based on the value of is_loading.
        """
        if is_loading:
            self.render_timer.start()
            self.issue_rgb25_button.start_loading()
            self.rgb_25_close_btn.setDisabled(True)
        else:
            self.issue_rgb25_button.stop_loading()
            self.rgb_25_close_btn.setDisabled(False)

    def show_asset_issued(self, asset_name):
        """This method handled after the asset issue"""
        header = 'Issue new ticker'
        title = 'You’re all set!'
        description = f"Asset '{asset_name}' has been issued successfully."
        home_button = 'Home'
        params = SuccessPageModel(
            header=header,
            title=title,
            description=description,
            button_text=home_button,
            callback=self._view_model.page_navigation.collectibles_asset_page,
        )
        self.render_timer.stop()
        self._view_model.page_navigation.show_success_page(params)
