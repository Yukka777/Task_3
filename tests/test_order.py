from selenium.webdriver.remote.webdriver import WebDriver

from pages.main_page import MainStellarBurgersPage

class TestOrdersPage:

    def test_open_order_from_list_order(self, driver: WebDriver, main_page, create_fake_user, register_user):
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
        # Нажать на кнопку оформления заказа
        order = constructor.click_order_button()
        # Проверка создания заказа
        order.check_order_number()
        # ПОЛУЧИТЬ НОМЕР ЗАКАЗА ИЗ ОКНА ЗАКАЗА
        order_number = order.get_order_number()
        print(f"Номер созданного заказа: {order_number}")
        # Закрыть окна оформления заказа через refresh
        driver.refresh()
        # Нажать на кпопку Лента заказов
        list_orders = personal_account.click_list_order_button()
        # Проверка появления текста Лента заказов
        list_orders.check_list_order_text()
        # Нажать на заказ
        personal_account.click_order()
        # Проверка открытия окна с заказом
        personal_account.check_order_window()

    def test_order_from_history_in_list(self, driver: WebDriver, main_page, create_fake_user, register_user):
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
        # Нажать на кнопку оформления заказа
        order = constructor.click_order_button()
        # Проверка создания заказа
        order.check_order_number()
        # Закрыть окна оформления заказа через refresh
        driver.refresh()
        # Нажать на кнопку Личного кабинета
        personal_account.click_personal_account()
        # Нажать на кнопку с историей заказов
        personal_account.click_order_history()
    
        # ПОЛУЧАЕМ НОМЕР ЗАКАЗА ИЗ ИСТОРИИ (а не из модального окна)
        order_number = personal_account.get_order_number()
        print(f"Номер заказа из истории: {order_number}")
    
        # Нажать на кпопку Лента заказов
        list_orders = personal_account.click_list_order_button()
        # Проверка появления текста Лента заказов
        list_orders.check_list_order_text()
        # Проверка присуствия созданного заказа
        personal_account.check_order_in_list(order_number)

    def test_orders_info(self, driver: WebDriver, main_page, create_fake_user, register_user):
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
        # Нажать на кпопку Лента заказов
        list_orders = personal_account.click_list_order_button()
        # Получения всех заказов до оформеления
        all_orders = list_orders.get_all_orders()
        # Получения всех заказов за текущий день до оформления
        all_orders_today = list_orders.get_all_orders_today()
        # Нажать на кнопку конструктора
        constructor = personal_account.click_constructor_button()
        # Добавление ингредиентов
        constructor.drag_to_element()
        # Нажать на кнопку оформления заказа
        order = constructor.click_order_button()
        # Проверка создания заказа
        order.check_order_number()
        # Закрыть окна оформления заказа через refresh
        driver.refresh()
        # Нажать на кнопку Личного кабинета
        personal_account.click_personal_account()
        # Нажать на кнопку с историей заказов
        personal_account.click_order_history()
    
        # ПОЛУЧАЕМ НОМЕР ЗАКАЗА ИЗ ИСТОРИИ
        order_number = personal_account.get_order_number()
        print(f"Номер заказа из истории: {order_number}")
    
        # Нажать на кпопку Лента заказов
        list_orders = personal_account.click_list_order_button()
        # Проверка изменения увелечения счетчика Выполнено за всё время
        list_orders.check_all_order(all_orders)
        # Проверка изменения увелечения счетчика Выполнено за сегодня
        list_orders.check_all_order_today(all_orders_today)
        # Проверка номера заказа - ИЩЕМ НАШ ЗАКАЗ В СПИСКЕ, а не сравниваем с первым
        list_orders.check_order_in_list(order_number)  # вместо check_order_in_work
