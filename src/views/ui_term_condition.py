# pylint: disable=too-many-instance-attributes, too-many-statements, unused-import
"""This module contains the TermConditionWidget class,
which represents the UI for Term Condition page.
"""
from __future__ import annotations

from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QSpacerItem
from PySide6.QtWidgets import QWidget

import src.resources_rc
from src.utils.helpers import load_stylesheet
from src.viewmodels.main_view_model import MainViewModel
from src.views.components.buttons import PrimaryButton
from src.views.components.buttons import SecondaryButton
from src.views.components.wallet_logo_frame import WalletLogoFrame


class TermConditionWidget(QWidget):
    """This class represents all the UI elements of the term and condition page."""

    def __init__(self, view_model):
        super().__init__()
        self._view_model: MainViewModel = view_model
        self.setObjectName('term_condition_page')
        self.setStyleSheet(
            load_stylesheet(
                'views/qss/term_condition_style.qss',
            ),
        )
        self.grid_layout_tnc = QGridLayout(self)
        self.grid_layout_tnc.setObjectName('gridLayout')
        self.tnc_horizontal_spacer = QSpacerItem(
            135,
            20,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum,
        )
        self.grid_layout_tnc.addItem(self.tnc_horizontal_spacer, 1, 0, 1, 1)
        self.horizontal_spacer_1 = QSpacerItem(
            135,
            20,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum,
        )
        self.grid_layout_tnc.addItem(self.horizontal_spacer_1, 2, 4, 1, 1)
        self.vertical_spacer_1 = QSpacerItem(
            20,
            178,
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding,
        )
        self.grid_layout_tnc.addItem(self.vertical_spacer_1, 0, 2, 1, 1)
        self.vertical_spacer_2 = QSpacerItem(
            20,
            177,
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding,
        )
        self.grid_layout_tnc.addItem(self.vertical_spacer_2, 3, 3, 1, 1)

        self.tnc_widget = QWidget(self)
        self.tnc_widget.setObjectName('TnCWidget')
        self.tnc_widget.setMinimumSize(QSize(696, 526))
        self.tnc_widget.setMaximumSize(QSize(696, 526))

        self.grid_layout_10_tnc = QGridLayout(self.tnc_widget)
        self.grid_layout_10_tnc.setObjectName('gridLayout_10')
        self.grid_layout_10_tnc.setContentsMargins(1, -1, 1, 25)

        self.tnc_line_tnc = QFrame(self.tnc_widget)
        self.tnc_line_tnc.setObjectName('TnC_line')
        self.tnc_line_tnc.setMinimumSize(QSize(690, 0))

        self.tnc_line_tnc.setFrameShape(QFrame.HLine)
        self.tnc_line_tnc.setFrameShadow(QFrame.Sunken)

        self.grid_layout_10_tnc.addWidget(self.tnc_line_tnc, 1, 0, 1, 1)

        self.tnc_text_desc = QPlainTextEdit(self.tnc_widget)
        self.tnc_text_desc.setObjectName('TnC_Text_Desc')
        self.tnc_text_desc.setMinimumSize(QSize(644, 348))
        self.tnc_text_desc.setMaximumSize(QSize(644, 348))
        self.tnc_text_desc.setStyleSheet(
            load_stylesheet('views/qss/q_label.qss'),
        )
        self.tnc_text_desc.setReadOnly(True)

        self.grid_layout_10_tnc.addWidget(
            self.tnc_text_desc, 2, 0, 1, 1, Qt.AlignHCenter,
        )

        self.grid_layout_11_tnc = QGridLayout()
        self.grid_layout_11_tnc.setObjectName('gridLayout_11')
        self.grid_layout_11_tnc.setContentsMargins(25, -1, 27, -1)

        self.tnc_label_text = QLabel(self.tnc_widget)
        self.tnc_label_text.setObjectName('welcome_text')
        self.tnc_label_text.setStyleSheet(
            load_stylesheet('views/qss/q_label.qss'),
        )

        self.grid_layout_11_tnc.addWidget(self.tnc_label_text, 0, 0, 1, 1)

        self.grid_layout_10_tnc.addLayout(self.grid_layout_11_tnc, 0, 0, 1, 1)

        self.tnc_horizontal_layout = QHBoxLayout()
        self.tnc_horizontal_layout.setSpacing(0)
        self.tnc_horizontal_layout.setObjectName('horizontalLayout_14')
        self.tnc_horizontal_layout.setContentsMargins(8, -1, 8, -1)

        self.decline_btn = SecondaryButton()
        self.decline_btn.setMinimumSize(QSize(318, 40))
        self.decline_btn.setMaximumSize(QSize(318, 40))

        self.tnc_horizontal_layout.addWidget(self.decline_btn)

        self.accept_btn = PrimaryButton()
        self.accept_btn.setMinimumSize(QSize(318, 40))
        self.accept_btn.setMaximumSize(QSize(318, 40))

        self.tnc_horizontal_layout.addWidget(self.accept_btn)

        self.grid_layout_10_tnc.addLayout(
            self.tnc_horizontal_layout,
            4,
            0,
            1,
            1,
        )

        self.vertical_spacer_tnc = QSpacerItem(
            20,
            40,
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding,
        )
        self.grid_layout_10_tnc.addItem(self.vertical_spacer_tnc, 3, 0, 1, 1)

        self.grid_layout_tnc.addWidget(self.tnc_widget, 1, 1, 2, 3)

        self.wallet_logo_tnc = WalletLogoFrame()
        self.grid_layout_tnc.addWidget(self.wallet_logo_tnc, 0, 0, 1, 2)

        self.retranslate_ui()
        self.setup_ui_connection()

    def setup_ui_connection(self):
        """Set up connections for UI elements."""
        self.accept_btn.clicked.connect(
            self._view_model.terms_view_model.on_accept_click,
        )
        self.decline_btn.clicked.connect(
            self._view_model.terms_view_model.on_decline_click,
        )

    # setupUi
    def retranslate_ui(self):
        """Retranslate the UI elements."""
        self.wallet_logo_tnc.logo_text.setText(
            QCoreApplication.translate(
                'iris_wallet_desktop',
                'iris_wallet',
                None,
            ),
        )
        self.tnc_label_text.setText(
            QCoreApplication.translate(
                'iris_wallet_desktop',
                'terms_and_conditions',
                None,
            ),
        )
        self.tnc_text_desc.setPlainText(
            QCoreApplication.translate(
                'iris_wallet_desktop',
                'terms_and_conditions_content',
                None,
            ),
        )
        self.decline_btn.setText(
            QCoreApplication.translate(
                'iris_wallet_desktop',
                'decline',
                None,
            ),
        )
        self.accept_btn.setText(
            QCoreApplication.translate(
                'iris_wallet_desktop',
                'accept',
                None,
            ),
        )