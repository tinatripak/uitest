from const import *
from basepage import *
from search import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(3)

driver.get(SITE)

main_page = SearchHelper(driver)
main_page.enter_search(SEARCH)
assert EXPECTED_RESULT in main_page.find_text()

driver.close()
