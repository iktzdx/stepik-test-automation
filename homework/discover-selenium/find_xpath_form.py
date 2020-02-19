import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, 'first_name')
    first_name.send_keys('Ivan')

    last_name = browser.find_element(By.NAME, 'last_name')
    last_name.send_keys('Petrov')

    city_info = browser.find_element(By.CLASS_NAME, 'city')
    city_info.send_keys('Smolensk')

    country_info = browser.find_element(By.ID, 'country')
    country_info.send_keys('Russia')

    submit_btn = browser.find_element(By.XPATH, '//button[text()=\'Submit\']')
    submit_btn.click()

finally:
    time.sleep(30)
    browser.quit()
