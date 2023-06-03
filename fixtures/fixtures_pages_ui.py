import pytest

from pages.google_page import GooglePage


@pytest.fixture(scope='function')
def google_page(browser):
    return GooglePage(browser=browser)
