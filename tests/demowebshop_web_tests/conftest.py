import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.base_url = 'https://demowebshop.tricentis.com'
    browser.config.window_width = 1000
    browser.config.window_height = 1100


    yield

    browser.quit()
