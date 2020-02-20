import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


links = ['http://suninjuly.github.io/registration1.html',
        'http://suninjuly.github.io/registration2.html']


def get_welcome_text(link):
    welcome_text = ''
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR,
                'div.first_block input.first[required]')
        last_name = browser.find_element(By.CSS_SELECTOR,
                'div.first_block input.second[required]')
        email = browser.find_element(By.CSS_SELECTOR,
                'div.first_block input.third[required]')

        first_name.send_keys('Daniel')
        last_name.send_keys('Kolomeets')
        email.send_keys('d.kolomeets@mail.test')

        submit_btn = browser.find_element(By.CSS_SELECTOR,
                'button[type="submit"].btn-default')
        submit_btn.click()

        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
    finally:
        browser.quit()
        return welcome_text


class TestWelcomeText(unittest.TestCase):
    def test_first_link(self):
        self.assertEqual(
                get_welcome_text(links[0]),
                'Congratulations! You have successfully registered!',
                'Registration is failed'
                )

    def test_second_link(self):
        self.assertEqual(
                get_welcome_text(links[1]),
                'Congratulations! You have successfully registered!',
                'Registration is failed'
                )


if __name__ == '__main__':
    unittest.main()
