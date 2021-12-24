from basepage import *
from selenium.webdriver.common.keys import Keys
from const import *
from basepage import *


class SearchHelper(BasePage):

    def enter_search(self, text):
        search_field = self.driver.find_element(By.CSS_SELECTOR, '[id = "gh-ac"]')
        search_field.send_keys(text, Keys.ENTER)
        return search_field

    def find_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class= "s-item__title"]').text

    def check_nav_bar(self):
        all_list = self.driver.find_elements(By.CSS_SELECTOR, '[class = "hl-cat-nav__container"]')
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu[0].split('\n')

    def click_on_bag_shop(self):

        return self.driver.find_element(By.CSS_SELECTOR, '[class= "gh-cart-icon"]').click()

    def show_bag_shop(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class= "font-title-3"]').text
