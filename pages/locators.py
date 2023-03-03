from selenium.webdriver.common.by import By


# Локаторы главной страницы
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SUCCES_MESSAGE = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success')

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '.register_form')


