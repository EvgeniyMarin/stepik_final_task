from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_login-username")  # ввод логина (почта)
    PASSWORD_LOGIN_INPUT = (By.CSS_SELECTOR, "#id_login-password")  # ввод пароля
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')  # кнопка войти
    REGISTRATION_INPUT_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')  # ввод логина (почта) для регистрации
    PASSWORD_REGISTRATION_INPUT_1 = (By.CSS_SELECTOR, "#id_registration-password1")  # ввод пароля для регистрации
    PASSWORD_REGISTRATION_INPUT_2 = (By.CSS_SELECTOR, "#id_registration-password2")  # повторный ввод пароля для регистрации
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')  # кнопка регистрации
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")             # форма логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")       # форма регистрации
