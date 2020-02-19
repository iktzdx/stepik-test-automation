import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(2)

    floated_button = browser.find_element(By.CLASS_NAME, 'trollface')
    floated_button.click()

    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    magic_number = browser.find_element(By.ID, 'input_value').text
    answer = calc(magic_number)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(answer)

    submit_btn = browser.find_element(By.CLASS_NAME, 'btn-primary')
    submit_btn.click()
finally:
    time.sleep(10)
    browser.quit()
