from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from const import SITE


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(3)

    pytest.page = Page(browser, SITE)

    try:
        yield browser

    finally:
        browser.quit()

    return browser
