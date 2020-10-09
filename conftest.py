import pytest

from pytest_allure_dsl import allure


pytest_plugins = ['pytest_allure_dsl']


def pytest_addoption(parser):
    parser.addoption(
        '--origin',
        action='store',
        default='https://www.******.uk',
        help='Base portal url (no slash in the end needed)',
    )


def pytest_configure(config):
    allure.environment(
        host=config.getoption('--origin')
    )


@pytest.fixture(scope='session')
def calculate_url(request):
    return f"{request.config.getoption('--origin')}/api/calculator/calculate/"
