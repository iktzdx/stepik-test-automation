import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_img = browser.find_element(By.ID, 'treasure')
    x_value = treasure_img.get_attribute("valuex")

    x = calc(x_value)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(x)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn-default')
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()
