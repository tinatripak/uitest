import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from const import *
from search import *
from basepage import *


def common_function():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(SITE)
    return driver


class Tests(TestCase):

    def test_search(self):
        driver = common_function()
        main_page = SearchHelper(driver)
        main_page.enter_search(SEARCH)
        assert EXPECTED_RESULT in main_page.find_text()

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
        assert EMPTY_BAG == text
