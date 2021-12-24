from selenium import webdriver
import pytest
from const import SITE


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(2)

    pytest.page = Page(browser, SITE)

    try:
        yield browser

    finally:
        browser.quit()

    return browser
