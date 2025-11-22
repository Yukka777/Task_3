from selenium.webdriver.remote.webdriver import WebDriver

from pages.main_page import MainStellarBurgersPage

class TestRecoveryPasswordPage:

    def test_personal_account(self, driver: WebDriver, main_page, create_fake_user, register_user):
        # Открыть главную страницу
        main_page = MainStellarBurgersPage(driver)
        # Нажать на кнопку Личного кабинета
        authorization_form = main_page.click_personal_account()
        # Ввод email
        authorization_form.input_email(create_fake_user["email"])
        # Ввод пароля
        authorization_form.input_password(create_fake_user["password"])
        # Нажать на кнопку Войти
        personal_account = authorization_form.click_entry_button()
        # Ожидание появления кнопки оформления заказа
        personal_account.check_order_button()

    def test_order_history(self, driver: WebDriver, main_page, create_fake_user, register_user):
        # Открыть главную страницу
        main_page = MainStellarBurgersPage(driver)
        # Нажать на кнопку Личного кабинета
        authorization_form = main_page.click_personal_account()
        # Ввод email
        authorization_form.input_email(create_fake_user["email"])
        # Ввод пароля
        authorization_form.input_password(create_fake_user["password"])
        # Нажать на кнопку Войти
        personal_account = authorization_form.click_entry_button()
        # Ожидание появления кнопки оформления заказа
        personal_account.check_order_button()
        # Нажать на кнопку Личного кабинета
        personal_account.click_personal_account()
        # Нажать на кнопку с историей заказов
        personal_account.click_order_history()
        # Проверка перехода на https://stellarburgers.nomoreparties.site/account/order-history
        personal_account.check_order_history_page()
        
    def test_exit(self, driver: WebDriver, main_page, create_fake_user, register_user):
        # Открыть главную страницу
        main_page = MainStellarBurgersPage(driver)
        # Нажать на кнопку Личного кабинета
        authorization_form = main_page.click_personal_account()
        # Ввод email
        authorization_form.input_email(create_fake_user["email"])
        # Ввод пароля
        authorization_form.input_password(create_fake_user["password"])
        # Нажать на кнопку Войти
        personal_account = authorization_form.click_entry_button()
        # Ожидание появления кнопки оформления заказа
        personal_account.check_order_button()
        # Нажать на кнопку Личного кабинета
        personal_account.click_personal_account()
        # Нажать на кнопку выход 
        personal_account.click_exit_button()
        # Проверка выхода из аккаунта
        authorization_form.check_entry_title()
