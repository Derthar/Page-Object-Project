from selenium.common import NoSuchElementException


# Базовый класс страницы
class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    # Проверка присутствия элемента на странице
    def is_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException as ex:
            print(ex)
            return False
        return True