from .base_page import BasePage
from .locators import LoginPageLocators

link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'

# Класс страницы логина/регистрации
class LoginPage(BasePage):
    def __init__(self, browser, link):
        self.link = link
        super().__init__(browser, self.link)

    # Проверка что это страница логина
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        return True

    # Проверка ссылки
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'This is not login url'

    # Проверка наличия формы логина
    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), 'There is no login form'

    # Проверка наличия формы регистраци
    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), 'There is no register form'