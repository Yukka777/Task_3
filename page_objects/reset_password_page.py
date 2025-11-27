from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ResetPasswordPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локаторы
    RESET_FORM = (By.XPATH, "//h2[text()='Восстановление пароля']")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")

    def check_reset_form_displayed(self):
        """Проверка отображения формы сброса пароля"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.RESET_FORM))
            return True
        except:
            return False

    def set_password(self, password):
        """Ввод нового пароля"""
        password_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(password)

    def click_show_password_button(self):
        """Нажатие кнопки показать пароль"""
        show_button = self.wait.until(EC.element_to_be_clickable(self.SHOW_PASSWORD_BUTTON))
        show_button.click()

    def click_hide_password_button(self):
        """Нажатие кнопки скрыть пароль (та же кнопка, что и показать)"""
        hide_button = self.wait.until(EC.element_to_be_clickable(self.SHOW_PASSWORD_BUTTON))
        hide_button.click()

    def check_password_field_highlighted(self):
        """Проверка подсветки поля пароля при активации"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD_ACTIVE))
            return True
        except:
            return False
