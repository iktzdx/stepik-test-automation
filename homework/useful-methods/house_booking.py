import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    right_price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
            )

    booking_button = WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.ID, 'book'))
            )
    booking_button.click()

    magic_number = browser.find_element(By.ID, 'input_value').text
    answer = calc(magic_number)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(magic_number)

    submit_button = WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                'button[type="submit"].btn-primary'))
            )
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
