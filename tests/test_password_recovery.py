from page_objects.main_page import MainPage
from page_objects.forgot_password_page import ForgotPasswordPage
from page_objects.account_page import AccountPage
import allure


class TestPasswordRecovery:

    @allure.title('Верификация перехода на страницу восстановления пароля')
    @allure.description('''
    Тестирование функциональности доступа к форме восстановления пароля:
    1. Активация элемента авторизации на главной странице
    2. Навигация к интерфейсу восстановления пароля через соответствующую ссылку
    3. Подтверждение отображения формы восстановления пароля
    ''')
    def test_navigate_to_password_recovery_page(self, navigate_to_password_recovery):
        """Тест использует фикстуру для перехода на страницу восстановления"""
        forgot_password_page = navigate_to_password_recovery
        assert forgot_password_page.check_recovery_form_displayed()

    @allure.title('Верификация процедуры восстановления пароля')
    @allure.description('''
    Тестирование процесса восстановления доступа к учетной записи:
    1. Навигация к интерфейсу восстановления пароля
    2. Ввод корректного email адреса зарегистрированного пользователя
    3. Активация процесса восстановления
    4. Подтверждение успешного перехода на этап сброса пароля
    ''')
    def test_password_recovery_with_email(self, navigate_to_password_recovery, registered_user):
        """Тест использует фикстуры для перехода и данных пользователя"""
        forgot_password_page = navigate_to_password_recovery
        user_email = registered_user['email']
        
        forgot_password_page.set_email(user_email)
        forgot_password_page.click_recover_button()
        forgot_password_page.wait_for_reset_page()
        
        assert forgot_password_page.check_reset_form_displayed()

    @allure.title('Верификация функционала отображения пароля')
    @allure.description('''
    Тестирование интерактивных элементов управления видимостью пароля:
    1. Навигация к интерфейсу авторизации через элемент личного кабинета
    2. Ввод тестовых данных в поле пароля
    3. Активация переключателя видимости пароля
    4. Подтверждение визуального выделения активного поля ввода
    ''')
    def test_show_hide_password_button_highlights_field(self, navigate_to_login_page):
        """Тест использует фикстуру для перехода на страницу логина"""
        account_page = navigate_to_login_page
        test_password = "TestPassword123"
        
        account_page.enter_password(test_password)
        account_page.click_show_password_button()
        assert account_page.check_password_field_highlighted()
