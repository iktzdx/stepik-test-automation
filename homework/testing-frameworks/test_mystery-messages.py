import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
    ]

mystery_message = ''

@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print(f'\nThe mystery message is: {mystery_message}')

@pytest.fixture(scope='function', autouse=True)
def calculate_answer():
    return math.log(int(time.time() + 113.7))

class TestFeedback(object):
    
    @pytest.mark.parametrize('url', links)
    def test_send_correct_answer(self, browser, calculate_answer, url):
        global mystery_message

        browser.get(url)

        textarea = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                    'textarea[required]'))
                )
        textarea.send_keys(str(calculate_answer))
        browser.find_element_by_css_selector('button.submit-submission').click()
        feedback_block = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                    'pre.smart-hints__hint'))
                )
        feedback_text = feedback_block.text
        
        if feedback_text != 'Correct!':
            mystery_message += feedback_text

        assert feedback_text == 'Correct!', f'The message is: {feedback_text}'
