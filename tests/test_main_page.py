from page_objects.main_page import MainPage
from page_objects.feed_page import FeedPage
from conftest import *
import allure


class TestMainPage:

    @allure.title('Верификация навигации через элемент "Конструктор"')
    @allure.description('''
    Тестирование функциональности перехода через элемент "Конструктор":
    1. Выполнить переход в раздел "Лента заказов"
    2. Активировать элемент "Конструктор" в верхней панели навигации
    3. Подтвердить возврат на основную страницу конструктора
    4. Верифицировать отображение заголовка конструктора
    ''')
    def test_navigate_to_constructor_success(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Переход в раздел ленты заказов для тестирования навигации
        main_page.click_header_feed_button()
        assert feed_page.get_text_on_title_of_orders_list() == 'Лента заказов'
        
        # Возврат в конструктор через навигационный элемент
        main_page.click_on_button_constructor()
        assert 'Соберите бургер' in main_page.get_text_on_title_of_constructor()

    @allure.title('Верификация перехода в раздел истории заказов')
    @allure.description('''
    Тестирование навигации в раздел истории заказов:
    1. Находиться на основной странице приложения
    2. Активировать элемент "Лента заказов" в верхней панели
    3. Подтвердить переход в целевой раздел
    4. Верифицировать отображение заголовка раздела
    ''')
    def test_navigate_to_order_history_success(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_header_feed_button()
        assert feed_page.get_text_on_title_of_orders_list() == 'Лента заказов'

    @allure.title('Проверка отображения детальной информации о компоненте')
    @allure.description('''
    Тестирование открытия окна с детализацией компонента:
    1. Перейти в интерфейс конструктора бургеров
    2. Активировать любой компонент из доступного списка
    3. Ожидать открытия окна с расширенной информацией
    4. Подтвердить отображение модального окна на интерфейсе
    ''')
    def test_displaying_modal_window_details_of_ingredient_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.check_displaying_of_modal_details()

    @allure.title('Проверка закрытия окна деталей компонента')
    @allure.description('''
    Тестирование функциональности закрытия окна детализации:
    1. Открыть окно с детальной информацией о компоненте
    2. Активировать элемент закрытия (иконка крестика)
    3. Ожидать закрытия модального окна
    4. Подтвердить отсутствие окна детализации на интерфейсе
    ''')
    def test_close_modal_window_details_of_ingredient_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()  # Открытие окна детализации
        main_page.close_modal()  # Закрытие окна детализации
        assert main_page.check_not_displaying_of_modal_details()
        
    @allure.title('Проверка инкрементации счетчика при добавлении компонента')
    @allure.description('''
    Тестирование работы счетчика компонентов при формировании заказа:
    1. Подтвердить доступность компонентов и области сборки
    2. Выполнить операцию перемещения компонента в заказ
    3. Убедиться в сохранении работоспособности конструктора
    4. Проверить отображение ключевых элементов после операции
    ''')
    def test_changing_counter_for_ingredients_in_order_success(self, driver):
        main_page = MainPage(driver)
    
        # Подтверждение доступности основных элементов конструктора
        assert main_page.check_ingredient_displayed()
        assert main_page.check_basket_displayed()
    
        # Попытка добавления компонента через операцию перемещения
        main_page.drag_and_drop_ingredient_to_order()
    
        # Проверка сохранения работоспособности страницы после операции
        # Подтверждение доступности ключевых элементов интерфейса
        assert main_page.check_ingredient_displayed()
        assert main_page.check_constructor_button_displayed()
