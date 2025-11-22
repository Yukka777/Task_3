import pytest

from config import Config
from helpers.delete_user import delete_user
from helpers.faker import fake_user
from helpers.reqistration_user import register_new_user_and_return_token
from api_requests.requests import Request
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.fixture(scope='class')
def create_fake_user():
    return fake_user()

@pytest.fixture(scope='class')
def register_user(create_fake_user):
    token = register_new_user_and_return_token(create_fake_user)
    yield
    delete_user(token)

@pytest.fixture(scope='session')
def client():
    return Request(Config.URL)

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser_name = request.param
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(10)
    yield driver
    # закрытие драйвера
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver: WebDriver):
    # открыть главную страницу
    driver.get(Config.URL)
