from selenium.webdriver.remote.webdriver import WebDriver

from pages.main_page import MainStellarBurgersPage

class TestOrderHistoryPage:

    def test_active_show_password_field(self, driver: WebDriver, main_page, create_fake_user):
        # Открыть главную страницу
        main_page = MainStellarBurgersPage(driver)
        # Нажать на кнопку Личного кабинета
        authorization_form = main_page.click_personal_account()
        # Нажать на кпопку Восстановить пароль
        recovery_form = authorization_form.click_recovery_password()
        # Ввод email
        recovery_form.input_email(create_fake_user["email"])
        # Нажать на кнопку Восстаносить
        recovery_form.click_recovery_button()
        # Проверить, что поле ввода пароля не показывает пароль
        recovery_form.check_inactive_show_button()
        # Нажать на поле для отображение пароля
        recovery_form.click_show_password_button()
        # Проверить, что поле ввода пароля показывает пароль
        recovery_form.check_active_show_button()
