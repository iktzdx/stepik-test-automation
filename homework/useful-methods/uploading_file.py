import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/file_input.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR,
            'input[name="firstname"]')
    last_name = browser.find_element(By.CSS_SELECTOR,
            'input[name="lastname"]')
    email = browser.find_element(By.CSS_SELECTOR,
            'input[name="email"]')
    upload_file = browser.find_element(By.CSS_SELECTOR,
            'input[type="file"]')
    submit_button = browser.find_element(By.CSS_SELECTOR,
            'button[type="submit"]')

    first_name.send_keys('Daniel')
    last_name.send_keys('Kolomeets')
    email.send_keys('d.kolomeets@mail.test')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    upload_file.send_keys(file_path)

    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
