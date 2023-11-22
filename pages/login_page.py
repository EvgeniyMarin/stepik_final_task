from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user()

    def should_be_login_url(self):
        """Проверка корректности url адреса"""
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert "login" in self.browser.current_url, "Не верный URL"

    def should_be_login_form(self):
        """Наличие формы логирования"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина отсутствует"

    def should_be_register_form(self):
        """Наличие формы регистрации"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации отсутствует"

    def register_new_user(self, email, password):
        """Регистрация нового пользователя"""
        self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_INPUT_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_INPUT_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()






