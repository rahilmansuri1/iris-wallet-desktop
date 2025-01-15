"""Unit test for Enter Help UI."""
# Disable the redefined-outer-name warning as
# it's normal to pass mocked objects in test functions
# pylint: disable=redefined-outer-name,unused-argument
from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QLabel

from src.viewmodels.main_view_model import MainViewModel
from src.views.ui_help import HelpWidget


@pytest.fixture
def help_page_navigation():
    """Fixture to create a mocked page navigation object."""
    mock_navigation = MagicMock()
    return mock_navigation


@pytest.fixture
def mock_help_view_model(help_page_navigation):
    """Fixture to create a MainViewModel instance with mocked page navigation."""
    return MainViewModel(help_page_navigation)


@pytest.fixture
def help_widget(mock_help_view_model):
    """Fixture to create a HelpWidget instance."""
    return HelpWidget(mock_help_view_model)


def test_retranslate_ui(help_widget: HelpWidget):
    """Test that the UI strings are correctly translated."""
    help_widget.retranslate_ui()

    assert help_widget.help_title_frame.title_name.text() == 'help'
    assert help_widget.help_title_label.text() == 'help'


def test_create_help_card(help_widget):
    """Test that a help card is created correctly with the given title, detail, and links."""
    title = 'Test Title'
    detail = 'Test Detail'
    links = ['http://example.com', 'http://example.org']

    help_card_frame = help_widget.create_help_card(title, detail, links)

    assert isinstance(help_card_frame, QFrame)
    assert help_card_frame.objectName() == 'help_card_frame'

    # Check that the title and detail are set correctly
    title_label = help_card_frame.findChild(QLabel, 'help_card_title_label')
    assert title_label.text() == title

    detail_label = help_card_frame.findChild(QLabel, 'help_card_detail_label')
    assert detail_label.text() == detail

    # Check that the links are set correctly
    for link in links:
        link_label = help_card_frame.findChild(QLabel, link)
        assert link_label.text() == f"<a style='color: #03CA9B;' href='{
            link
        }'>{link}</a>"
