# pylint: disable=too-many-instance-attributes, too-many-statements, unused-import
"""This module contains the WalletOrTransferSelectionWidget class,
which represents the UI for wallet or transfer selection methods.
"""
from __future__ import annotations

from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtGui import QIcon
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QSpacerItem
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

import src.resources_rc
from src.data.repository.setting_repository import SettingRepository
from src.model.enums.enums_model import AssetType
from src.model.enums.enums_model import LoaderDisplayModel
from src.model.enums.enums_model import TransferStatusEnumModel
from src.model.enums.enums_model import TransferType
from src.model.enums.enums_model import WalletType
from src.model.selection_page_model import AssetDataModel
from src.model.selection_page_model import SelectionPageModel
from src.utils.clickable_frame import ClickableFrame
from src.utils.helpers import load_stylesheet
from src.viewmodels.main_view_model import MainViewModel
from src.views.components.loading_screen import LoadingTranslucentScreen
from src.views.components.wallet_logo_frame import WalletLogoFrame


class WalletOrTransferSelectionWidget(QWidget):
    """This class represents all the UI elements of the wallet or transfer selection page."""

    def __init__(self, view_model, params):
        super().__init__()
        self.setStyleSheet(
            load_stylesheet(
                'views/qss/wallet_or_transfer_selection_style.qss',
            ),
        )
        self.__loading_translucent_screen = None
        self._view_model: MainViewModel = view_model
        self._params: SelectionPageModel = params
        self.asset_type = None
        if self._params.rgb_asset_page_load_model:
            self.asset_type = self._params.rgb_asset_page_load_model.asset_type
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setObjectName('grid_layout')
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.wallet_logo = WalletLogoFrame()
        self.grid_layout.addWidget(self.wallet_logo, 0, 0, 1, 2)

        self.vertical_spacer_1 = QSpacerItem(
            20, 208, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding,
        )

        self.grid_layout.addItem(self.vertical_spacer_1, 0, 3, 1, 1)

        self.horizontal_spacer_1 = QSpacerItem(
            268, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum,
        )

        self.grid_layout.addItem(self.horizontal_spacer_1, 1, 0, 1, 1)

        self.widget_page = QWidget(self)
        self.widget_page.setObjectName('widget_page')
        self.widget_page.setMinimumSize(QSize(660, 400))
        self.widget_page.setMaximumSize(QSize(696, 526))

        self.vertical_layout = QVBoxLayout(self.widget_page)
        self.vertical_layout.setSpacing(6)
        self.vertical_layout.setObjectName('vertical_layout_9')
        self.vertical_layout.setContentsMargins(1, 11, 1, 10)

        self.header_horizontal_layout = QHBoxLayout()
        self.header_horizontal_layout.setObjectName('header_horizontal_layout')
        self.header_horizontal_layout.setContentsMargins(0, 0, 20, 0)

        self.title_text = QLabel(self.widget_page)
        self.title_text.setObjectName('title_text')
        self.title_text.setMinimumSize(QSize(0, 50))
        self.title_text.setMaximumSize(QSize(16777215, 50))

        self.header_horizontal_layout.addWidget(self.title_text)

        self.close_button = QPushButton(self.widget_page)
        self.close_button.setObjectName('close_button')
        self.close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_button.setMinimumSize(QSize(24, 24))
        self.close_button.setMaximumSize(QSize(50, 65))
        self.close_button.setAutoFillBackground(False)

        close_icon = QIcon()
        close_icon.addFile(
            ':/assets/x_circle.png',
            QSize(), QIcon.Normal, QIcon.Off,
        )
        self.close_button.setIcon(close_icon)
        self.close_button.setIconSize(QSize(24, 24))
        self.close_button.setCheckable(False)
        self.close_button.setChecked(False)
        self.header_horizontal_layout.addWidget(self.close_button)

        self.vertical_layout.addLayout(self.header_horizontal_layout)

        self.header_line = QFrame(self.widget_page)
        self.header_line.setObjectName('line_2')

        self.header_line.setFrameShape(QFrame.Shape.HLine)
        self.header_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.vertical_layout.addWidget(self.header_line)

        self.vertical_spacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding,
        )

        self.vertical_layout.addItem(self.vertical_spacer_2)

        self.select_option_layout = QHBoxLayout()
        self.select_option_layout.setObjectName('select_option_layout')
        self.select_option_layout.setContentsMargins(-1, -1, -1, 0)
        self.option_1_frame = ClickableFrame(
            self._params.logo_1_title, self._params.callback,
        )
        self.option_1_frame.setObjectName('option_1_frame')
        self.option_1_frame.setMinimumSize(QSize(220, 200))
        self.option_1_frame.setMaximumSize(QSize(220, 200))

        self.option_1_frame.setFrameShape(QFrame.StyledPanel)
        self.option_1_frame.setFrameShadow(QFrame.Raised)
        self.option_1_frame_grid_layout = QGridLayout(self.option_1_frame)
        self.option_1_frame_grid_layout.setSpacing(0)
        self.option_1_frame_grid_layout.setObjectName('gridLayout_27')
        self.option_1_frame_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.option_2_logo = QLabel(self.option_1_frame)
        self.option_2_logo.setObjectName('option_2_logo')
        self.option_2_logo.setMinimumSize(QSize(100, 100))
        self.option_2_logo.setMaximumSize(QSize(100, 100))
        self.option_2_logo.setStyleSheet('border:none')
        self.option_2_logo.setPixmap(QPixmap(self._params.logo_1_path))

        self.option_1_frame_grid_layout.addWidget(
            self.option_2_logo, 0, 0, 1, 1, Qt.AlignHCenter,
        )

        self.option_1_text_label = QLabel(self.option_1_frame)
        self.option_1_text_label.setObjectName('option_1_text_label')
        self.option_1_text_label.setMinimumSize(QSize(0, 30))
        self.option_1_text_label.setMaximumSize(QSize(16777215, 30))

        self.option_1_frame_grid_layout.addWidget(
            self.option_1_text_label, 1, 0, 1, 1, Qt.AlignHCenter,
        )

        self.select_option_layout.addWidget(self.option_1_frame)

        self.option_2_frame = ClickableFrame(
            self._params.logo_2_title, self.widget_page, self._params.callback,
        )
        self.option_2_frame.setObjectName('frame_8')
        self.option_2_frame.setMinimumSize(QSize(220, 200))
        self.option_2_frame.setMaximumSize(QSize(220, 200))

        self.option_2_frame.setFrameShape(QFrame.StyledPanel)
        self.option_2_frame.setFrameShadow(QFrame.Raised)
        self.option_2_frame_grid_layout = QGridLayout(self.option_2_frame)
        self.option_2_frame_grid_layout.setSpacing(0)
        self.option_2_frame_grid_layout.setObjectName('grid_layout_28')
        self.option_2_frame_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.option_1_logo_label = QLabel(self.option_2_frame)
        self.option_1_logo_label.setObjectName('option_1_logo_label')
        self.option_1_logo_label.setMaximumSize(QSize(100, 100))
        self.option_1_logo_label.setStyleSheet('border:none')
        self.option_1_logo_label.setPixmap(QPixmap(self._params.logo_2_path))

        self.option_2_frame_grid_layout.addWidget(
            self.option_1_logo_label, 0, 0, 1, 1,
        )

        self.option_2_text_label = QLabel(self.option_2_frame)
        self.option_2_text_label.setObjectName('option_2_text_label')
        self.option_2_text_label.setMinimumSize(QSize(0, 30))
        self.option_2_text_label.setMaximumSize(QSize(16777215, 30))

        self.option_2_frame_grid_layout.addWidget(
            self.option_2_text_label, 1, 0, 1, 1, Qt.AlignHCenter,
        )

        self.select_option_layout.addWidget(self.option_2_frame)

        self.vertical_layout.addLayout(self.select_option_layout)

        self.vertical_spacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding,
        )

        self.vertical_layout.addItem(self.vertical_spacer_3)

        self.grid_layout.addWidget(self.widget_page, 1, 1, 2, 3)

        self.horizontal_spacer_2 = QSpacerItem(
            268, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum,
        )

        self.grid_layout.addItem(self.horizontal_spacer_2, 2, 4, 1, 1)

        self.vertical_spacer_4 = QSpacerItem(
            20, 208, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding,
        )

        self.grid_layout.addItem(self.vertical_spacer_4, 3, 2, 1, 1)

        ln_message = QApplication.translate(
            'iris_wallet_desktop', 'ln_message', 'Starting LN node',
        )
        self.__loading_translucent_screen = LoadingTranslucentScreen(
            parent=self, description_text=ln_message, dot_animation=True, loader_type=LoaderDisplayModel.FULL_SCREEN,
        )
        self.retranslate_ui()
        self.setup_ui_connection()

    def retranslate_ui(self):
        """Retranslate the UI elements."""
        self.title_text.setText(
            QCoreApplication.translate(
                'iris_wallet_desktop', self._params.title, None,
            ),
        )
        self.option_1_text_label.setText(
            QCoreApplication.translate(
                'iris_wallet_desktop', self._params.logo_1_title, None,
            ),
        )
        self.option_2_text_label.setText(
            QCoreApplication.translate(
                'iris_wallet_desktop', self._params.logo_2_title, None,
            ),
        )

    def setup_ui_connection(self):
        """Set up connections for UI elements."""
        self.option_1_frame.clicked.connect(self.handle_frame_click)
        self.option_2_frame.clicked.connect(self.handle_frame_click)
        self._view_model.wallet_transfer_selection_view_model.ln_node_process_status.connect(
            self.show_wallet_loading_screen,
        )
        self.close_button.clicked.connect(self.close_button_navigation)

    def handle_frame_click(self, _id):
        """Handle the click event for the option_frame_1 and option_frame_2."""

        # Retrieve the transfer type from the parameters
        transfer_type = self._params.callback
        # Handle the 'embedded' frame click event
        if _id == WalletType.EMBEDDED_TYPE_WALLET.value:
            SettingRepository.set_wallet_type(WalletType.EMBEDDED_TYPE_WALLET)
            self._view_model.wallet_transfer_selection_view_model.start_node_for_embedded_option()

        # Handle the 'connect' frame click event
        elif _id == WalletType.CONNECT_TYPE_WALLET.value:
            SettingRepository.set_wallet_type(WalletType.CONNECT_TYPE_WALLET)
            self._view_model.page_navigation.ln_endpoint_page(
                'wallet_selection_page',
            )

        # Handle the 'On chain' frame click event
        elif _id == TransferType.ON_CHAIN.value:
            # Navigate to the appropriate page based on the transfer type
            if transfer_type == TransferStatusEnumModel.RECEIVE.value:
                self._view_model.page_navigation.receive_rgb25_page(
                    params=AssetDataModel(
                        asset_type=self.asset_type, asset_id=self._params.asset_id,
                    ),
                )
            elif transfer_type == TransferStatusEnumModel.SEND.value:
                self._view_model.page_navigation.send_rgb25_page()
            elif transfer_type == TransferStatusEnumModel.SEND_BTC.value:
                self._view_model.page_navigation.send_bitcoin_page()
            elif transfer_type == TransferStatusEnumModel.RECEIVE_BTC.value:
                self._view_model.page_navigation.receive_bitcoin_page()

        # Handle the 'Off chain' frame click event
        elif _id == TransferType.LIGHTNING.value:
            # Navigate to the send or receive LN invoice page based on the transfer type
            if transfer_type in (TransferStatusEnumModel.SEND.value, TransferStatusEnumModel.SEND_BTC.value):
                self._view_model.page_navigation.send_ln_invoice_page(
                    self.asset_type,
                )
            elif transfer_type in (TransferStatusEnumModel.RECEIVE.value, TransferStatusEnumModel.RECEIVE_BTC.value):
                self._view_model.page_navigation.create_ln_invoice_page(
                    self._params.asset_id,
                    self._params.asset_name,
                    self.asset_type,
                )

    def show_wallet_loading_screen(self, status):
        """This method handled show loading screen on wallet selection page"""
        if status is True:
            self.option_1_frame.setDisabled(True)
            self.option_2_frame.setDisabled(True)
            self.__loading_translucent_screen.start()
        if not status:
            self.option_1_frame.setDisabled(False)
            self.option_2_frame.setDisabled(False)
            self.__loading_translucent_screen.stop()

    def close_button_navigation(self):
        """
        Handles navigation to the previous page, emitting asset information if available.
        """
        if self._params.back_page_navigation is not None:
            self._params.back_page_navigation()

            if self._params.rgb_asset_page_load_model is not None:
                self._view_model.rgb25_view_model.asset_info.emit(
                    self._params.rgb_asset_page_load_model.asset_id,
                    self._params.rgb_asset_page_load_model.asset_name,
                    self._params.rgb_asset_page_load_model.image_path,
                    self._params.rgb_asset_page_load_model.asset_type,
                )