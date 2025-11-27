from page_objects.main_page import MainPage
from page_objects.forgot_password_page import ForgotPasswordPage
from page_objects.account_page import AccountPage
from urls import Urls
import allure


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_navigate_to_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        
        driver.get(Urls.BASE_URL)
        main_page.click_login_account_button()
        main_page.click_recover_password_link()
        assert forgot_password_page.check_recovery_form_displayed()

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_password_recovery_with_email(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        
        user_credentials = create_new_user_and_delete[0]
        user_email = user_credentials['email']
        
        driver.get(Urls.BASE_URL)
        main_page.click_login_account_button()
        main_page.click_recover_password_link()
        forgot_password_page.set_email(user_email)
        forgot_password_page.click_recover_button()
        
        # Используем метод ожидания из Page Object
        forgot_password_page.wait_for_reset_page()
        
        # Проверяем переход
        assert forgot_password_page.check_reset_form_displayed()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_hide_password_button_highlights_field(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        
        driver.get(Urls.BASE_URL)
        main_page.click_on_personal_account_in_header()
        test_password = "TestPassword123"
        account_page.enter_password(test_password)
        account_page.click_show_password_button()
        assert account_page.check_password_field_highlighted()
