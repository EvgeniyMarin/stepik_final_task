from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import pytest
link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        """Тест перехода на страницу логина"""
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        """Тест наличия кнопки логирования/регистрации"""
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_url_address_matching(browser):
    """Тест корректности url адреса"""
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_url()


def test_availability_of_a_login_form(browser):
    """Тест наличия формы логирования"""
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_form()


def test_availability_of_a_register_form(browser):
    """Тест наличия формы регистрации"""
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """Тест перехода в корзину и проверки, что она пуста"""
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.basket_is_empty()
