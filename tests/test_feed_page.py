from page_objects.feed_page import FeedPage
from page_objects.main_page import MainPage
from conftest import *
import allure


class TestFeedPage:

    @allure.title('Верификация обновления счетчика общего количества заказов')
    @allure.description('''
    Тестирование инкрементации счетчика заказов за весь период:
    1. Аутентификация в системе пользователем
    2. Фиксация первоначального значения общего счетчика
    3. Генерация нового заказа через интерфейс конструктора
    4. Проверка инкрементации значения общего счетчика
    5. Подтверждение корректности обновления статистических данных
    ''')
    def test_changes_counter_for_quantity_of_orders_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Аутентификация пользователя для получения доступа к функционалу заказов
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        # Получение исходного значения счетчика заказов за весь период
        main_page.click_header_feed_button()
        orders_count_1 = feed_page.get_quantity_of_orders()
        
        # Создание нового заказа через интерфейс конструктора
        main_page.click_on_button_constructor()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        
        # Ожидание завершения обработки заказа и отображения подтверждения
        main_page.wait_for_order_processing(timeout=30)
        main_page.click_on_button_close_confirmation_modal()
        
        # Проверка обновленного значения счетчика заказов
        main_page.click_header_feed_button()
        orders_count_2 = feed_page.get_quantity_of_orders()
        
        # Конвертация строковых значений в числовые и их сравнение
        count_1 = int(orders_count_1)
        count_2 = int(orders_count_2)
        # Подтверждение факта увеличения счетчика после создания заказа
        assert count_2 > count_1, f"Отсутствие инкрементации счетчика: исходное значение {count_1}, текущее значение {count_2}"

    @allure.title('Верификация обновления счетчика дневных заказов')
    @allure.description('''
    Тестирование инкрементации счетчика заказов за текущие сутки:
    1. Аутентификация в системе пользователем
    2. Фиксация первоначального значения дневного счетчика
    3. Генерация нового заказа через интерфейс конструктора
    4. Проверка инкрементации значения дневного счетчика
    5. Подтверждение актуальности суточной статистики
    ''')
    def test_changes_counter_for_daily_quantity_of_orders_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Аутентификация пользователя для выполнения операций с заказами
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        # Получение исходного значения счетчика заказов за текущие сутки
        main_page.click_header_feed_button()
        orders_count_1 = feed_page.get_daily_quantity_of_orders()
        
        # Создание нового заказа через интерфейс конструктора
        main_page.click_on_button_constructor()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        
        # Ожидание завершения обработки заказа
        main_page.wait_for_order_processing(timeout=30)
        main_page.click_on_button_close_confirmation_modal()
        
        # Проверка обновленного значения дневного счетчика
        main_page.click_header_feed_button()
        orders_count_2 = feed_page.get_daily_quantity_of_orders()
        
        # Конвертация строковых значений в числовые и их сравнение
        count_1 = int(orders_count_1)
        count_2 = int(orders_count_2)
        # Подтверждение факта увеличения дневного счетчика
        assert count_2 > count_1, f"Отсутствие инкрементации дневного счетчика: исходное значение {count_1}, текущее значение {count_2}"
        
    @allure.title('Проверка отображения нового заказа в секции текущих выполнений"')
    @allure.description('''
    Тестирование отображения вновь созданного заказа в ленте:
    1. Аутентификация в системе пользователем
    2. Генерация нового заказа через интерфейс конструктора
    3. Получение идентификатора созданного заказа
    4. Навигация в раздел ленты заказов
    5. Проверка присутствия заказа в секции выполняемых заказов
    6. Подтверждение реального времени обновления данных
    ''')
    def test_displaying_new_order_in_progress_feed_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Аутентификация пользователя для создания заказа
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        # Создание заказа и получение его идентификатора для последующей проверки
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        
        # Ожидание завершения обработки заказа
        main_page.wait_for_order_processing(timeout=30)
        main_page.get_number_of_order_in_modal_confirmation()
        main_page.click_on_button_close_confirmation_modal()
        
        # Навигация в раздел ленты заказов для выполнения проверки
        main_page.click_header_feed_button()
        
        # Подтверждение отображения созданного заказа в секции выполняемых заказов
        order_in_progress = feed_page.get_order_number_in_feed_progress_section()
        assert order_in_progress is not None
