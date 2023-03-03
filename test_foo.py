import time

import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


@pytest.mark.usefixtures
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_lesson3_step2(browser, link='http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'):
    page = BasePage(browser=browser, url=link)
    page.open()
    item_name = page.browser.find_element(By.CSS_SELECTOR, '.product_main h1').text
    item_value = page.browser.find_element(By.CSS_SELECTOR, '.product_main p').text
    page.browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg').click()
    page.solve_quiz_and_get_code()
    actual_name = page.browser.find_element(By.CSS_SELECTOR, '.alertinner strong').text
    actual_value = page.browser.find_element(By.CSS_SELECTOR, '.alertinner p strong').text
    assert item_name == actual_name, 'Имена товаров не совпадают'
    assert item_value == actual_value, 'Стоимости товаров не совпадают'
    time.sleep(100)
