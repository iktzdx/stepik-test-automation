import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    magic_button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    magic_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    magic_number = browser.find_element(By.ID, 'input_value').text
    answer = calc(magic_number)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(answer)

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_btn.click()
finally:
    time.sleep(12)
    browser.quit()
