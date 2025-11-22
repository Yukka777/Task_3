from selenium.webdriver.remote.webdriver import WebDriver

from pages.main_page import MainStellarBurgersPage

class TestMainFunctionsPage:

    def test_cunstructor(self, driver: WebDriver, main_page, create_fake_user, register_user):
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
        # Нажать на кпопку Конструктор
        constructor = personal_account.click_constructor_button()
        # Проверка появления текста Соберите бургер
        constructor.check_constructor_text()

    def test_list_order(self, driver: WebDriver, main_page, create_fake_user, register_user):
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
        # Нажать на кпопку Лента заказов
        list_orders = personal_account.click_list_order_button()
        # Проверка появления текста Лента заказов
        list_orders.check_list_order_text()

    def test_ingredient_form(self, driver: WebDriver, main_page, create_fake_user, register_user):
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
        # Нажать на кпопку Конструктор
        constructor = personal_account.click_constructor_button()
        # Нажать на ингредиент
        ingredient = constructor.select_ingredient()
        # Проверить, что открылось окно ингредиента
        ingredient.check_ingredient_form_title()
        # Закрыть окно ингредиента
        ingredient.close_ingredient_form()
        # Проверка появления текста Соберите бургер
        constructor.check_constructor_text()

    def test_add_ingredient_to_order(self, driver: WebDriver, main_page, create_fake_user, register_user):
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
        # Нажать на кпопку Конструктор
        constructor = personal_account.click_constructor_button()
        # Добавление ингредиента в заказ
        constructor.drag_to_element()
        # Проверка добавления ингредиента
        constructor.check_count_buns()

    def test_make_order(self, driver: WebDriver, main_page, create_fake_user, register_user):
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
        # Нажать на кпопку Конструктор
        constructor = personal_account.click_constructor_button()
        # Добавление ингредиента в заказ
        constructor.drag_to_element()
        # Проверка добавления ингредиента
        constructor.check_count_buns()
        # Нажать на кнопку оформления заказа
        order = constructor.click_order_button()
        # Проверка создания заказа
        order.check_order_number()
