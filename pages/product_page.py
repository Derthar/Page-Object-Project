from .base_page import BasePage
from .locators import MainPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, link):
        self.link = link
        super().__init__(browser, self.link)

    def should_be_succes_message(self):
        assert self.is_present(*MainPageLocators.SUCCESS_MESSAGE), 'Succes message is present'

    def should_not_be_succes_message(self):
        assert self.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE), 'Succes message is present'
