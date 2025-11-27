from page_objects.main_page import MainPage
from page_objects.forgot_password_page import ForgotPasswordPage
from page_objects.reset_password_page import ResetPasswordPage
import allure


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля')
    @allure.description('''
    Тестирование перехода на страницу восстановления пароля:
    1. Нажатие на кнопку "Войти в аккаунт" на главной странице
    2. Нажатие на ссылку "Восстановить пароль" на форме входа
    3. Проверка успешного перехода на страницу восстановления пароля
    ''')
    def test_navigate_to_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        
        # Переход на страницу восстановления пароля
        main_page.click_login_account_button()
        main_page.click_recover_password_link()
        
        # Проверка что мы на странице восстановления пароля
        assert forgot_password_page.check_recovery_form_displayed()

    @allure.title('Восстановление пароля: ввод email и отправка формы')
    @allure.description('''
    Тестирование процесса восстановления пароля:
    1. Переход на страницу восстановления пароля
    2. Ввод email в поле для восстановления
    3. Нажатие кнопки "Восстановить"
    4. Проверка перехода на страницу сброса пароля
    ''')
    def test_password_recovery_with_email(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        
        # Получение email зарегистрированного пользователя
        user_credentials = create_new_user_and_delete[0]
        user_email = user_credentials['email']
        
        # Переход на страницу восстановления пароля
        main_page.click_login_account_button()
        main_page.click_recover_password_link()
        
        # Ввод email и отправка формы
        forgot_password_page.set_email(user_email)
        forgot_password_page.click_recover_button()
        
        # Проверка перехода на страницу сброса пароля
        assert reset_password_page.check_reset_form_displayed()

    @allure.title('Активация поля пароля кнопкой показать/скрыть пароль')
    @allure.description('''
    Тестирование функционала показа/скрытия пароля:
    1. Переход на страницу сброса пароля
    2. Ввод пароля в поле
    3. Нажатие на кнопку показать/скрыть пароль
    4. Проверка активации (подсветки) поля пароля
    ''')
    def test_show_hide_password_button_highlights_field(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        
        # Получение данных пользователя
        user_credentials = create_new_user_and_delete[0]
        user_email = user_credentials['email']
        new_password = "NewPassword123"
        
        # Переход на страницу сброса пароля
        main_page.click_login_account_button()
        main_page.click_recover_password_link()
        forgot_password_page.set_email(user_email)
        forgot_password_page.click_recover_button()
        
        # Ввод пароля и проверка функционала показа/скрытия
        reset_password_page.set_password(new_password)
        
        # Нажатие на кнопку показать пароль и проверка подсветки
        reset_password_page.click_show_password_button()
        assert reset_password_page.check_password_field_highlighted()
        
        # Нажатие на кнопку скрыть пароль
        reset_password_page.click_hide_password_button()
