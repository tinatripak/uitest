from basepage import *
from selenium.webdriver.common.keys import Keys


class SearchHelper(BasePage):

    def enter_search(self, text):
        search_field = self.driver.find_element_by_css_selector('[id= "gh-ac"]')
        search_field.send_keys(text, Keys.ENTER)
        return search_field

    def find_text(self):
        return self.driver.find_element_by_css_selector('[class= "s-item__title"]').text
