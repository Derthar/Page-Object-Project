from selenium.webdriver.common.by import By


# Локаторы базовой страницы
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a.btn.btn-default')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, 'div#content_inner p')


# Локаторы главной страницы
class MainPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert')  # '.alert.alert-safe.alert-noicon.alert-success')
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')


# Локаторы страницы регистрации
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '.register_form')


# Локаторы страницы корзины
class BasketPageLocators:
    BASKET_HEADER = (By.CSS_SELECTOR, 'div h1')
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
