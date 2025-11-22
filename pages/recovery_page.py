import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class RecoveryPage (BasePage):
    RECOVERY_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@type='password']")
    SHOW_PASSWORD = (By.XPATH, ".//div[contains(@class,'input_type_password ')]")
    ACTIVE_SHOW_PASSWORD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@type='text']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Нажать на кнопку Восстановить')
    def click_recovery_button(self):
        self.waiting_visibility_element(self.RECOVERY_BUTTON)
        self.click(self.RECOVERY_BUTTON)

    @allure.step('Нажать на кнопку Показать пароль')
    def click_show_password_button(self):
        self.waiting_clickable(self.SHOW_PASSWORD)
        self.click(self.SHOW_PASSWORD)

    @allure.step('Проверка активности поля Пароль')
    def check_active_show_button(self):
        assert self.waiting_visibility_element(self.ACTIVE_SHOW_PASSWORD)

    @allure.step('Проверка неактивности поля Пароль')
    def check_inactive_show_button(self):
        assert self.waiting_invisibility_element(self.ACTIVE_SHOW_PASSWORD)

    @allure.step('Ввод email')
    def input_email(self, email):
        self.input_text(self.EMAIL_FIELD, email)
