# pylint: disable=redefined-outer-name
"""
Custom Pytest Configuration for Wallet Mode Testing
"""
from __future__ import annotations

import pytest

DEFAULT_WALLET_MODES = ['embedded', 'connect']  # Default wallet modes


def pytest_addoption(parser):
    """
    Add custom command-line options for pytest to select wallet mode.

    :param parser: Pytest parser object
    """
    parser.addoption(
        '--wallet-mode',
        action='store',
        choices=DEFAULT_WALLET_MODES,
        help="Set wallet mode to 'embedded' or 'connect'. If not provided, tests run for both modes.",
    )


def pytest_generate_tests(metafunc):
    """
    Dynamically run tests for both wallet modes if --wallet-mode is not provided.

    :param metafunc: Pytest metafunction object
    """
    if 'wallet_mode' in metafunc.fixturenames:
        wallet_mode = metafunc.config.getoption('wallet_mode')
        if wallet_mode:
            # Run for the specified mode
            metafunc.parametrize('wallet_mode', [wallet_mode])
        else:
            # Run for both modes
            metafunc.parametrize('wallet_mode', DEFAULT_WALLET_MODES)


@pytest.fixture(scope='session')
def wallet_mode(request):
    """
    Fixture to provide the selected wallet mode.

    :param request: Pytest request object
    :return: Selected wallet mode
    """
    return request.param


def pytest_runtest_setup(item):
    """Skip tests based on wallet mode."""
    wallet_mode = item.config.getoption('--wallet-mode')

    # Skip tests marked with @pytest.mark.skip_for_embedded if running in embedded mode
    if wallet_mode == 'embedded' and any(mark.name == 'skip_for_embedded' for mark in item.own_markers):
        pytest.skip(
            'Skipping test because it is not applicable in embedded mode.',
        )

    # Skip tests marked with @pytest.mark.skip_for_connect if running in connect mode
    if wallet_mode == 'connect' and any(mark.name == 'skip_for_connect' for mark in item.own_markers):
        pytest.skip(
            'Skipping test because it is not applicable in connect mode.',
        )
