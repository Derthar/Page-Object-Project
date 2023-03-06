from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")


# Локаторы главной страницы
class MainPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert')  # '.alert.alert-safe.alert-noicon.alert-success')
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '.register_form')
