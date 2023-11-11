from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def adding_to_basket(self):
        """Метод добавления товара в корзину"""
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def checking_the_addition_to_basket(self):
        """Метод для проверки соответствия названия товара в корзине и на странице товара"""
        text_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        text_product_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_THE_ADDED_PRODUCT_BASKET).text
        assert text_product == text_product_in_basket, "Имя товара в корзине не соответствует имени со страницы товара"

    def checking_price_compliance(self):
        """Метод для проверки соответствия цены товара и стоимости корзины"""
        text_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        text_price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_BASKET).text
        print(f"цена товара: {text_price}, стоимость корзины: {text_price_in_basket}")
        assert text_price == text_price_in_basket, "Цена товара и стоимость корзины ОТЛИЧАЕТСЯ"
        
        


    """Дописать методы проверки"""

