import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r'C:\Users\Кристина\Desktop\chromedriver.exe')
browser.get("https://www.ebay.com/")
browser.implicitly_wait(20)

search_term = "piano"
browser.find_element_by_css_selector('[id= "gh-ac"]').send_keys(search_term)
time.sleep(2)
browser.find_element_by_css_selector('[id= "gh-ac"]').send_keys(Keys.ENTER)
time.sleep(2)

actual_text = browser.find_element_by_css_selector('[class= "s-item__title"]').text
time.sleep(2)

assert actual_text == '61 Keys Electronic Teaching Keyboard Digital Music Piano Instrument & Microphone'
browser.close()