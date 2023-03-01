import time

import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage


# link = "http://selenium1py.pythonanywhere.com/"
# link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer'


# def go_to_login_page(browser):
#     browser.get(link)
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()


@pytest.mark.usefixtures
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser)
    page.open()
    page.go_to_login_page()
    time.sleep(10)


def test_guest_should_see_login_link(browser):
    page = MainPage(browser)
    page.open()
    page.should_be_login_link()
    time.sleep(10)


def test_lign_page(browser):
    page = LoginPage(browser)
    page.open()
    page.should_be_login_page()
