import time
import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.locators import MainPageLocators


link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


@pytest.mark.skip
@pytest.mark.usefixtures
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_lesson3_step2(browser, link):
    page = BasePage(browser=browser, url=link)
    page.open()
    page.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE)
    item_name = page.browser.find_element(By.CSS_SELECTOR, '.product_main h1').text
    item_value = page.browser.find_element(By.CSS_SELECTOR, '.product_main p').text
    page.browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg').click()
    page.solve_quiz_and_get_code()
    page.is_appeared(*MainPageLocators.SUCCESS_MESSAGE)
    actual_name = page.browser.find_element(By.CSS_SELECTOR, '.alertinner strong').text
    actual_value = page.browser.find_element(By.CSS_SELECTOR, '.alertinner p strong').text
    assert item_name == actual_name, 'Имена товаров не совпадают'
    assert item_value == actual_value, 'Стоимости товаров не совпадают'
    time.sleep(1)


@pytest.mark.usefixtures
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    page.browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg').click()
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE)


@pytest.mark.usefixtures
def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, link)
    page.open()
    assert page.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE)


@pytest.mark.usefixtures
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    assert page.is_disappeared(*MainPageLocators.SUCCESS_MESSAGE)
