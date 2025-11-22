import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from pages.personal_account_page import PersonalAccountPage
from pages.recovery_page import RecoveryPage

class AuthorizationPage (BasePage):
    RECOVERY_PASSWORD = (By.XPATH, ".//a[text()='Восстановить пароль']")
    EMAIL_FIELD = (By.XPATH, ".//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']")
    ENTRY_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    ENTRY_TITLE = (By.XPATH, ".//h2[text()='Вход']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Нажать на кнопку Восстановить пароль')
    def click_recovery_password(self):
        self.waiting_visibility_element(self.RECOVERY_PASSWORD)
        self.click(self.RECOVERY_PASSWORD)
        return RecoveryPage(self.driver)

    @allure.step('Ввод email')
    def input_email(self, email):
        self.input_text(self.EMAIL_FIELD, email)
        
    @allure.step('Ввод password')
    def input_password(self, password):
        self.input_text(self.PASSWORD_FIELD, password)

    @allure.step('Нажать на кнопку Войти')
    def click_entry_button(self):
        self.waiting_clickable(self.ENTRY_BUTTON)
        self.click(self.ENTRY_BUTTON)
        return PersonalAccountPage(self.driver)
    
    @allure.step('Проверка заголовка Вход')
    def check_entry_title(self):
        assert self.waiting_text_in_element(self.ENTRY_TITLE, "Вход")
