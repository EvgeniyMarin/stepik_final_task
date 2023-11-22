from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")   # кнопка перехода на форму логирования/регистрации
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")   # некорректный селектор для негативных тестов
    BUTTON_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn-default")   # кнопка перехода в корзину
    USER_ICON = (By.CSS_SELECTOR, ".icon-user") # иконка юзера


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_login-username")     # ввод логина (почта)
    PASSWORD_LOGIN_INPUT = (By.CSS_SELECTOR, "#id_login-password")      # ввод пароля
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')       # кнопка войти
    REGISTRATION_INPUT_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')      # ввод логина (почта) для регистрации
    PASSWORD_REGISTRATION_INPUT_1 = (By.CSS_SELECTOR, "#id_registration-password1")     # ввод пароля для регистрации
    PASSWORD_REGISTRATION_INPUT_2 = (By.CSS_SELECTOR, "#id_registration-password2")     # повторный ввод пароля для регистрации
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')  # кнопка регистрации
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")             # форма логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")       # форма регистрации


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '[type="submit"].btn-lg')      # кнопка добавления в корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner .product_main > h1")     # имя товара на странице
    NAME_OF_THE_ADDED_PRODUCT_BASKET = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner strong")      # имя добавленного товара в корзину
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")     # цена товара
    PRICE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert > .alertinner > p > strong")    # стоимость корзины


class BasketPageLocators:
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")    # сообщение внутри корзины