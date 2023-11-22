from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        """Метод проверки сообщения корзины(пустая корзина)"""
        assert self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE), "Корзина не пуста"