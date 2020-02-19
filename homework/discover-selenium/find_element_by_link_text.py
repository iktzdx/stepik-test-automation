import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/find_link_text'
search_query = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    secret_link = browser.find_element(By.LINK_TEXT, search_query)
    secret_link.click()

    first_name = browser.find_element(By.NAME, 'first_name')
    first_name.send_keys('Ivan')

    last_name = browser.find_element(By.NAME, 'last_name')
    last_name.send_keys('Petrov')

    city_info = browser.find_element(By.CLASS_NAME, 'city')
    city_info.send_keys('Smolensk')

    country_info = browser.find_element(By.ID, 'country')
    country_info.send_keys('Russia')

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type=\'submit\']')
    submit_btn.click()

finally:
    time.sleep(30)
    browser.quit()
