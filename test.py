import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from const import SITE, EXPECTED_RESULT, SEARCH, EMPTY_BAG
from search import SearchHelper
from basepage import BasePage


def common_function():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(SITE)
    return driver


class Tests(TestCase):

    def test_search(self):
        driver = common_function()
        main_page = SearchHelper(driver)
        main_page.enter_search(SEARCH)

        assert EXPECTED_RESULT.lower() in main_page.find_text().lower()

    def test_navbar(self):
        driver = common_function()
        main_page = SearchHelper(driver)
        elements = main_page.check_nav_bar()

        assert "Fashion" and "Health & Beauty" in elements

    def test_shop_bag(self):
        driver = common_function()
        main_page = SearchHelper(driver)
        main_page.click_on_bag_shop()
        text = main_page.show_bag_shop()

        assert EMPTY_BAG.lower() == text.lower()
