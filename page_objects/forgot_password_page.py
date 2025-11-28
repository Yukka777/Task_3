from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.forgot_password_locators import ForgotPasswordLocators
import allure


class ForgotPasswordPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Проверить отображение формы восстановления пароля')
    def check_recovery_form_displayed(self):
        """Проверка отображения формы восстановления пароля"""
        try:
            self.wait.until(EC.visibility_of_element_located(ForgotPasswordLocators.RECOVERY_FORM))
            return True
        except:
            return False

    @allure.step('Ввести email для восстановления: {email}')
    def set_email(self, email):
        """Ввод email в поле для восстановления"""
        email_field = self.wait.until(EC.element_to_be_clickable(ForgotPasswordLocators.EMAIL_FIELD))
        email_field.clear()
        email_field.send_keys(email)

    @allure.step('Нажать кнопку "Восстановить"')
    def click_recover_button(self):
        """Нажатие кнопки 'Восстановить'"""
        recover_button = self.wait.until(EC.element_to_be_clickable(ForgotPasswordLocators.RECOVER_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView();", recover_button)
        recover_button.click()

    @allure.step('Нажать на ссылку "Войти"')
    def click_back_to_login_link(self):
        """Нажатие на ссылку возврата к форме входа"""
        back_link = self.wait.until(EC.element_to_be_clickable(ForgotPasswordLocators.BACK_TO_LOGIN_LINK))
        back_link.click()

    @allure.step('Проверить переход на страницу сброса пароля')
    def check_reset_form_displayed(self):
        """Проверка перехода на страницу сброса пароля"""
        # Используем URL из локаторов
        current_url = self.driver.current_url
        return ForgotPasswordLocators.RESET_PASSWORD_URL in current_url

    @allure.step('Дождаться перехода на страницу сброса пароля')
    def wait_for_reset_page(self, timeout=10):
        """Ожидание перехода на страницу сброса пароля"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.url_contains(ForgotPasswordLocators.RESET_PASSWORD_URL))
