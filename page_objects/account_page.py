from page_objects.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
import allure

class AccountPage(BasePage):
    # Действия с формой аутентификации
    
    @allure.step('Заполнить поле email')
    def enter_email(self, email):
        """Ввод адреса электронной почты в соответствующее поле"""
        self.send_keys_to_input(AccountPageLocators.INPUT_EMAIL, email)
    
    @allure.step('Заполнить поле пароля')
    def enter_password(self, password):
        """Ввод пароля в предназначенное для этого поле"""
        self.send_keys_to_input(AccountPageLocators.INPUT_PASSWORD, password)
    
    @allure.step('Выполнить авторизацию"')
    def click_login_button(self):
        """Активация кнопки для выполнения входа в систему"""
        self.click_on_element(AccountPageLocators.BUTTON_LOGIN)
    
    @allure.step('Проверить видимость формы входа')
    def check_login_page_displayed(self):
        """Проверка отображения интерфейса авторизации"""
        return self.check_displaying_of_element(AccountPageLocators.LOGIN_TITLE)

    @allure.step('Дождаться появления кнопки регистрации"')
    def wait_visibility_of_button_register(self):
        """Ожидание отображения элемента регистрации на странице"""
        self.wait_visibility_of_element(AccountPageLocators.BUTTON_REGISTER)

    @allure.step('Проверить доступность кнопки регистрации"')
    def check_displaying_of_button_register(self):
        """Подтверждение наличия элемента регистрации на странице"""
        return self.check_displaying_of_element(AccountPageLocators.BUTTON_REGISTER)

    # === МЕТОДЫ ЛИЧНОГО КАБИНЕТА ===
    
    @allure.step('Проверить наличие кнопки выхода из системы"')
    def check_logout_button_displayed(self):
        """Проверка отображения элемента для завершения сеанса"""
        return self.check_displaying_of_element(AccountPageLocators.BUTTON_LOGOUT)

    @allure.step('Активировать выход из профиля')
    def click_on_logout_button(self):
        """Выполнение действия по завершению пользовательской сессии"""
        self.click_on_element(AccountPageLocators.BUTTON_LOGOUT)
