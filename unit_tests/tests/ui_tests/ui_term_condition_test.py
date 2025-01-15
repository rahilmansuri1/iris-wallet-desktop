"""Unit test for TermConditionWidget."""
# Disable the redefined-outer-name warning as
# it's normal to pass mocked objects in test functions
# pylint: disable=redefined-outer-name,unused-argument
from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from src.viewmodels.main_view_model import MainViewModel
from src.views.ui_term_condition import TermConditionWidget


@pytest.fixture
def term_condition_widget(qtbot):
    """Fixture to create and return an instance of TermConditionWidget."""
    mock_navigation = MagicMock()
    view_model = MagicMock(MainViewModel(mock_navigation))
    widget = TermConditionWidget(view_model)
    qtbot.addWidget(widget)
    return widget


def test_retranslate_ui(term_condition_widget: TermConditionWidget):
    """Test the retranslation of UI elements in TermConditionWidget."""
    term_condition_widget.retranslate_ui()

    assert term_condition_widget.tnc_label_text.text() == 'terms_and_conditions'
    assert term_condition_widget.tnc_text_desc.toPlainText(
    ) == 'terms_and_conditions_content'
