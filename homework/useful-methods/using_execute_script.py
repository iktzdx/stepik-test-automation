import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element(By.ID, 'input_value').text
    x = calc(x_value)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(x)

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robot_radiobutton = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);',
            robot_radiobutton)
    robot_radiobutton.click()

    robot_submit = browser.find_element(By.CSS_SELECTOR,
            'button[type="submit"].btn-primary')
    robot_submit.click()

finally:
    time.sleep(9)
    browser.quit()
    
