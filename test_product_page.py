# import time
import pytest
from pages.locators import MainPageLocators
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage


main_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.xfail
@pytest.mark.usefixtures
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, main_link)
    page.open()
    page.browser.find_element(*MainPageLocators.ADD_TO_BASKET).click()
    assert page.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE)


@pytest.mark.usefixtures
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, main_link)
    page.open()
    assert page.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE)


@pytest.mark.xfail
@pytest.mark.usefixtures
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, main_link)
    page.open()
    page.browser.find_element(*MainPageLocators.ADD_TO_BASKET).click()
    assert page.is_disappeared(*MainPageLocators.SUCCESS_MESSAGE)


@pytest.mark.usefixtures
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, main_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.usefixtures
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, main_link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, link=browser.current_url)
    page.should_be_login_link()