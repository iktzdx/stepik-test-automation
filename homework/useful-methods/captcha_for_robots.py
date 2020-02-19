import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    
    browser.get('http://suninjuly.github.io/math.html')
    
    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x_element.text
    answer = calc(x)
    
    answer_area = browser.find_element(By.ID, 'answer')
    answer_area.send_keys(answer)
    
    captcha_checkbox = browser.find_element(By.CSS_SELECTOR, 'label[for="robotCheckbox"]')
    captcha_checkbox.click()
    
    captcha_radiobutton = browser.find_element(By.CSS_SELECTOR, 'label[for="robotsRule"]')
    captcha_radiobutton.click()
    
    captcha_submit = browser.find_element(By.CLASS_NAME, 'btn-default')
    captcha_submit.click()

finally:
    time.sleep(10)
    browser.quit()
