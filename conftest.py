import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: en, ru ...")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    driver_browser = webdriver.Chrome(options=options)
    driver_browser.get(link)
    yield driver_browser
    driver_browser.quit()
