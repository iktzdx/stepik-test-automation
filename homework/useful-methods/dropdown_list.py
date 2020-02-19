import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#link = 'http://suninjuly.github.io/selects1.html'
link = 'https://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_num = browser.find_element(By.ID, 'num1')
    second_num = browser.find_element(By.ID, 'num2')

    answer = int(first_num.text) + int(second_num.text)

    dropdown_list = Select(browser.find_element(By.ID, 'dropdown'))
    correct_option = dropdown_list.select_by_value(str(answer))

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn-default')
    submit_btn.click()

finally:
    time.sleep(9)
    browser.quit()
