from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from const import SITE


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = SITE

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f"Can not find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(expected_conditions.presence_of_all_elements_located(locator),
                                                       message=f"Can not  find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)
