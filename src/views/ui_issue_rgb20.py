# pylint: disable=too-many-instance-attributes, too-many-statements, unused-import
"""This module contains the IssueRGB20Widget class,
 which represents the UI for issuing RGB20 assets.
"""
from __future__ import annotations

from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QSpacerItem
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

import src.resources_rc
from src.model.success_model import SuccessPageModel
from src.utils.common_utils import set_number_validator
from src.utils.common_utils import set_placeholder_value
from src.utils.constant import IRIS_WALLET_TRANSLATIONS_CONTEXT
from src.utils.helpers import load_stylesheet
from src.utils.render_timer import RenderTimer
from src.viewmodels.main_view_model import MainViewModel
from src.views.components.buttons import PrimaryButton
from src.views.components.wallet_logo_frame import WalletLogoFrame


class IssueRGB20Widget(QWidget):
    """This class represents the UI for issuing RGB20 assets."""

    def __init__(self, view_model):
        super().__init__()
        self.render_timer = RenderTimer(task_name='IssueRGB20Asset Rendering')
        self._view_model: MainViewModel = view_model
        self.setStyleSheet(load_stylesheet('views/qss/issue_rgb20_style.qss'))
        self.setObjectName('issue_rgb20_page')
        self.issue_rgb20_grid_layout = QGridLayout(self)
        self.issue_rgb20_grid_layout.setObjectName('issue_rgb20_grid_layout')
        self.issue_rgb20_wallet_logo = WalletLogoFrame(self)

        self.issue_rgb20_grid_layout.addWidget(
            self.issue_rgb20_wallet_logo, 0, 0, 1, 2,
        )

        self.horizontal_spacer_rgb20_widget = QSpacerItem(
            265,
            20,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum,
        )

        self.issue_rgb20_grid_layout.addItem(
            self.horizontal_spacer_rgb20_widget, 1, 3, 1, 1,
        )

        self.vertical_spacer_rgb20_widget = QSpacerItem(
            20,
            190,
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding,
        )

        self.issue_rgb20_grid_layout.addItem(
            self.vertical_spacer_rgb20_widget, 3, 1, 1, 1,
        )

        self.horizontal_spacer_2 = QSpacerItem(
            266,
            20,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum,
        )

        self.issue_rgb20_grid_layout.addItem(
            self.horizontal_spacer_2, 2, 0, 1, 1,
        )

        self.issue_rgb20_vertical_spacer_1 = QSpacerItem(
            20,
            190,
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding,
        )

        self.issue_rgb20_grid_layout.addItem(
            self.issue_rgb20_vertical_spacer_1, 0, 2, 1, 1,
        )

        self.issue_rgb_20_widget = QWidget(self)
        self.issue_rgb_20_widget.setObjectName(
            'issue_rgb20_widget',
        )
        self.issue_rgb_20_widget.setMinimumSize(QSize(499, 608))
        self.issue_rgb_20_widget.setMaximumSize(QSize(466, 608))

        self.inner_grid_layout = QGridLayout(self.issue_rgb_20_widget)
        self.inner_grid_layout.setSpacing(6)
        self.inner_grid_layout.setObjectName('inner_grid_layout')
        self.inner_grid_layout.setContentsMargins(1, 4, 1, 30)
        self.vertical_layout_issue_rgb20 = QVBoxLayout()
        self.vertical_layout_issue_rgb20.setSpacing(6)
        self.vertical_layout_issue_rgb20.setObjectName(
            'vertical_layout_setup_wallet_password',
        )
        self.issue_rgb20_title_layout = QHBoxLayout()
        self.issue_rgb20_title_layout.setObjectName('horizontal_layout_1')
        self.issue_rgb20_title_layout.setContentsMargins(35, 9, 40, 0)
        self.issue_rgb20_title = QLabel(
            self.issue_rgb_20_widget,
        )
        self.issue_rgb20_title.setObjectName(
            'set_wallet_password_label',
        )
        self.issue_rgb20_title.setMinimumSize(QSize(415, 63))

        self.issue_rgb20_title_layout.addWidget(self.issue_rgb20_title)

        self.rgb_20_close_btn = QPushButton(self.issue_rgb_20_widget)
        self.rgb_20_close_btn.setObjectName('rgb_20_close_btn')
        self.rgb_20_close_btn.setMinimumSize(QSize(24, 24))
        self.rgb_20_close_btn.setMaximumSize(QSize(50, 65))
        self.rgb_20_close_btn.setAutoFillBackground(False)

        issue_rgb20_close_icon = QIcon()
        issue_rgb20_close_icon.addFile(
            ':/assets/x_circle.png',
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.rgb_20_close_btn.setIcon(issue_rgb20_close_icon)
        self.rgb_20_close_btn.setIconSize(QSize(24, 24))
        self.rgb_20_close_btn.setCheckable(False)
        self.rgb_20_close_btn.setChecked(False)

        self.issue_rgb20_title_layout.addWidget(
            self.rgb_20_close_btn, 0, Qt.AlignHCenter,
        )

        self.vertical_layout_issue_rgb20.addLayout(
            self.issue_rgb20_title_layout,
        )

        self.header_line = QFrame(self.issue_rgb_20_widget)
        self.header_line.setObjectName('line_3')

        self.header_line.setFrameShape(QFrame.HLine)
        self.header_line.setFrameShadow(QFrame.Sunken)

        self.vertical_layout_issue_rgb20.addWidget(self.header_line)

        self.asset_ticker_layout = QVBoxLayout()
        self.asset_ticker_layout.setSpacing(0)
        self.asset_ticker_layout.setObjectName('vertical_layout_1')
        self.asset_ticker_layout.setContentsMargins(60, -1, 0, -1)

        self.asset_ticker_label = QLabel(self.issue_rgb_20_widget)
        self.asset_ticker_label.setObjectName('asset_ticker_label')
        self.asset_ticker_label.setMinimumSize(QSize(0, 35))
        self.asset_ticker_label.setBaseSize(QSize(0, 0))
        self.asset_ticker_label.setAutoFillBackground(False)
        self.asset_ticker_label.setFrameShadow(QFrame.Plain)
        self.asset_ticker_label.setLineWidth(1)

        self.asset_ticker_layout.addWidget(self.asset_ticker_label)

        self.short_identifier_input = QLineEdit(
            self.issue_rgb_20_widget,
        )
        self.short_identifier_input.setObjectName('issue_rgb20_input')
        self.short_identifier_input.setMinimumSize(QSize(0, 40))
        self.short_identifier_input.setMaximumSize(QSize(370, 40))

        self.short_identifier_input.setFrame(False)
        self.short_identifier_input.setClearButtonEnabled(False)

        self.asset_ticker_layout.addWidget(self.short_identifier_input)

        self.vertical_layout_issue_rgb20.addLayout(
            self.asset_ticker_layout,
        )

        self.asset_name_layout = QVBoxLayout()
        self.asset_name_layout.setSpacing(0)
        self.asset_name_layout.setObjectName('vertical_layout_2')
        self.asset_name_layout.setContentsMargins(60, -1, 0, -1)

        self.asset_name_label = QLabel(self.issue_rgb_20_widget)
        self.asset_name_label.setObjectName('asset_name_label')
        self.asset_name_label.setMinimumSize(QSize(0, 40))
        self.asset_name_label.setMaximumSize(QSize(370, 40))
        self.asset_name_layout.addWidget(self.asset_name_label)

        self.asset_name_input = QLineEdit(
            self.issue_rgb_20_widget,
        )
        self.asset_name_input.setObjectName('asset_name_input')
        self.asset_name_input.setMinimumSize(QSize(0, 40))
        self.asset_name_input.setMaximumSize(QSize(370, 40))

        self.asset_name_input.setFrame(False)
        self.asset_name_input.setClearButtonEnabled(False)

        self.asset_name_layout.addWidget(self.asset_name_input)

        self.vertical_layout_issue_rgb20.addLayout(
            self.asset_name_layout,
        )
        self.asset_supply_layout = QVBoxLayout()
        self.asset_supply_layout.setSpacing(0)
        self.asset_supply_layout.setObjectName('vertical_layout_3')
        self.asset_supply_layout.setContentsMargins(60, -1, 0, -1)

        self.total_supply_label = QLabel(self.issue_rgb_20_widget)
        self.total_supply_label.setObjectName('total_supply_label')
        self.total_supply_label.setMinimumSize(QSize(0, 40))
        self.total_supply_label.setMaximumSize(QSize(370, 40))
        self.asset_supply_layout.addWidget(self.total_supply_label)

        self.amount_input = QLineEdit(
            self.issue_rgb_20_widget,
        )
        self.amount_input.setObjectName('amount_input')
        self.amount_input.setMinimumSize(QSize(0, 40))
        self.amount_input.setMaximumSize(QSize(370, 40))
        set_number_validator(self.amount_input)
        self.amount_input.setFrame(False)
        self.amount_input.setClearButtonEnabled(False)

        self.asset_supply_layout.addWidget(self.amount_input)

        self.vertical_layout_issue_rgb20.addLayout(
            self.asset_supply_layout,
        )

        self.vertical_spacer_issue_rgb20 = QSpacerItem(
            20,
            40,
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding,
        )

        self.vertical_layout_issue_rgb20.addItem(
            self.vertical_spacer_issue_rgb20,
        )

        self.footer_line = QFrame(self.issue_rgb_20_widget)
        self.footer_line.setObjectName('bottom_line_frame')

        self.footer_line.setFrameShape(QFrame.HLine)
        self.footer_line.setFrameShadow(QFrame.Sunken)

        self.vertical_layout_issue_rgb20.addWidget(self.footer_line)

        self.issue_button_spacer = QSpacerItem(
            20, 22, QSizePolicy.Preferred, QSizePolicy.Preferred,
        )
        self.vertical_layout_issue_rgb20.addItem(self.issue_button_spacer)
        self.issue_rgb20_btn = PrimaryButton()
        self.issue_rgb20_btn.setMinimumSize(QSize(402, 40))
        self.issue_rgb20_btn.setMaximumSize(QSize(402, 40))

        self.issue_rgb20_btn.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor),
        )
        self.vertical_layout_issue_rgb20.addWidget(
            self.issue_rgb20_btn, 0, Qt.AlignCenter,
        )

        self.inner_grid_layout.addLayout(
            self.vertical_layout_issue_rgb20,
            0,
            0,
            1,
            1,
        )

        self.issue_rgb20_grid_layout.addWidget(
            self.issue_rgb_20_widget,
            1,
            1,
            2,
            2,
        )

        self.setup_ui_connection()
        self.retranslate_ui()

    def setup_ui_connection(self):
        """Set up connections for UI elements."""
        self.asset_name_input.textChanged.connect(self.handle_button_enabled)
        self.short_identifier_input.textChanged.connect(
            self.handle_button_enabled,
        )
        self.amount_input.textChanged.connect(self.handle_button_enabled)
        self.rgb_20_close_btn.clicked.connect(
            self._view_model.issue_rgb20_asset_view_model.on_close_click,
        )
        self._view_model.issue_rgb20_asset_view_model.issue_button_clicked.connect(
            self.update_loading_state,
        )
        self.issue_rgb20_btn.clicked.connect(self.on_issue_rgb20_click)
        self._view_model.issue_rgb20_asset_view_model.is_issued.connect(
            self.asset_issued,
        )
        self.amount_input.textChanged.connect(
            lambda: set_placeholder_value(self.amount_input),
        )

    def retranslate_ui(self):
        """Retranslate the UI elements."""
        self.issue_rgb20_btn.setDisabled(True)
        self.issue_rgb20_title.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT,
                'issue_new_rgb20_asset',
                None,
            ),
        )
        self.asset_ticker_label.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT,
                'asset_ticker',
                None,
            ),
        )
        self.short_identifier_input.setPlaceholderText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT,
                'short_identifier',
                None,
            ),
        )
        self.asset_name_label.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT,
                'asset_name',
                None,
            ),
        )
        self.asset_name_input.setPlaceholderText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT,
                'name_of_the_asset',
                None,
            ),
        )
        self.total_supply_label.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT,
                'total_supply',
                None,
            ),
        )
        self.amount_input.setPlaceholderText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT,
                'amount_to_issue',
                None,
            ),
        )
        self.issue_rgb20_btn.setText(
            QCoreApplication.translate(
                IRIS_WALLET_TRANSLATIONS_CONTEXT, 'issue_asset', None,
            ),
        )

    def update_loading_state(self, is_loading: bool):
        """
            Updates the loading state of the issue_rgb20_btn.
            This method prints the loading state and starts or stops the loading animation
            of the proceed_wallet_password object based on the value of is_loading.
        """
        if is_loading:
            self.render_timer.start()
            self.issue_rgb20_btn.start_loading()
            self.rgb_20_close_btn.setDisabled(True)
        else:
            self.render_timer.stop()
            self.issue_rgb20_btn.stop_loading()
            self.rgb_20_close_btn.setDisabled(False)

    def on_issue_rgb20_click(self):
        """Handle the click event for issuing a new RGB20 asset."""
        # Retrieve text values from input fields
        short_identifier = self.short_identifier_input.text().upper()
        asset_name = self.asset_name_input.text()
        amount_to_issue = self.amount_input.text()

        # Call the view model method and pass the text values as arguments
        self._view_model.issue_rgb20_asset_view_model.on_issue_click(
            short_identifier,
            asset_name,
            amount_to_issue,
        )

    def handle_button_enabled(self):
        """Updates the enabled state of the send button."""
        if (self.short_identifier_input.text() and self.amount_input.text() and self.asset_name_input.text() and self.amount_input.text() != '0'):
            self.issue_rgb20_btn.setDisabled(False)
        else:
            self.issue_rgb20_btn.setDisabled(True)

    def asset_issued(self, asset_name):
        """This method handled after channel created"""
        header = 'Issue new ticker'
        title = 'You’re all set!'
        description = f"Asset '{asset_name}' has been issued successfully."
        button_text = 'Home'
        params = SuccessPageModel(
            header=header,
            title=title,
            description=description,
            button_text=button_text,
            callback=self._view_model.page_navigation.fungibles_asset_page,
        )
        self.render_timer.stop()
        self._view_model.page_navigation.show_success_page(params)
