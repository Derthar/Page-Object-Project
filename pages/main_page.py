from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser, link):
        super().__init__(browser, link)

    def go_to_login_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link").click()
