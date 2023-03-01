from .locators import MainPageLocators
from .base_page import BasePage


# Класс главной страницы
class MainPage(BasePage):
    def __init__(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/'
        super().__init__(browser, self.link)

    # Проверка наличия ссылки логина
    def should_be_login_link(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented!"
                                        # * нужна для распаковки кортежа

    # Переход на страницу логина
    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
