from selenium.webdriver.common.by import By

EXPECTED_RESULT = '61 Keys Electronic Teaching Keyboard Digital Music Piano Instrument & Microphone'
SEARCH = "piano"
SITE = "https://www.ebay.com/"
EMPTY_BAG = "You don't have any items in your cart."


class Locators:
    NAV_BAR_CLASS = (By.CSS_SELECTOR, '[class = "hl-cat-nav__container"]')
    CLICK_BUTTON_CLASS = (By.CSS_SELECTOR, '[class= "gh-cart-icon"]')
    SHOW_BAG_CLASS = (By.CSS_SELECTOR, '[class= "font-title-3"]')
    SEARCH_ID = (By.CSS_SELECTOR, '[id = "gh-ac"]')
    FIND_TEXT_CLASS = (By.CSS_SELECTOR, '[class= "s-item__title"]')
