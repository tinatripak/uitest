from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from const import Locators
from basepage import BasePage


class SearchHelper(BasePage):

    def enter_search(self, text):
        return self.driver.find_element(By.ID, Locators.SEARCH_ID).send_keys(text, Keys.ENTER)

    def find_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, Locators.FIND_TEXT_CLASS).text

    def show_bag_shop(self):
        return self.driver.find_element(By.CLASS_NAME, Locators.SHOW_BAG_CLASS).text

    def click_on_bag_shop(self):
        return self.driver.find_element(By.CLASS_NAME, Locators.CLICK_BUTTON_CLASS).click()

    def check_nav_bar(self):
        all_list = self.driver.find_elements(By.CLASS_NAME, Locators.NAV_BAR_CLASS)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]

        return nav_bar_menu[0].split('\n')
