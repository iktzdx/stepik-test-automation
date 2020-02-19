import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUniqSelectors(unittest.TestCase):
    def test_link(self):
        #link = 'http://suninjuly.github.io/registration1.html'
        link = 'http://suninjuly.github.io/registration2.html'

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

            self.assertEqual('Congratulations! You have successfully registered!',
                    welcome_text, 'Welcome text found')
        finally:
            time.sleep(10)
            browser.quit()


if __name__ == '__main__':
    unittest.main()
