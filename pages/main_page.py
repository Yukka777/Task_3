import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.authorization_page import AuthorizationPage
from pages.base_page import BasePage

class MainStellarBurgersPage(BasePage):
    ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Нажать на Личный кабинет')
    def click_personal_account(self):
        self.waiting_clickable(self.ACCOUNT)
        self.click(self.ACCOUNT)
        return AuthorizationPage(self.driver)
