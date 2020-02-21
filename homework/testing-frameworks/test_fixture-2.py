import pytest
from selenium import webdriver


link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture
def browser():
    print('\nstart browser for test…')
    browser = webdriver.Chrome()
    # отсутствует browser.quit(), поэтому экземпляры браузера закрываются
    # только после окончания всех тестов
    return browser


class TestMainPage1():
    # фикстура передана в качестве аргумента
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('#login_link')

    # для каждого теста запускается отдельный экземпляр браузера
    def test_guest_should_see_baskeet_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('.basket-mini .btn-group > a')
