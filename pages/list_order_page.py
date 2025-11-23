import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

from pages.base_page import BasePage


class ListOrderPage(BasePage):
    LIST_ORDER_TEXT = (By.XPATH, "//h1[text()='Лента заказов']")
    ALL_ORDERS = (By.XPATH, ".//div[p[text()='Выполнено за все время:'] and p[contains(@class, 'OrderFeed_number__2MbrQ')]]")
    ORDER_TODAY = (By.XPATH, ".//div[p[text()='Выполнено за сегодня:'] and p[contains(@class, 'OrderFeed_number__2MbrQ')]]")
    IN_WORK_ORDER = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[contains(@class, 'text_type_digits-default')]")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Ожидание появления текста Лента заказов')
    def check_list_order_text(self):
        assert self.waiting_text_in_element(self.LIST_ORDER_TEXT, "Лента заказов")

    @allure.step('Получение всех заказов до оформления')
    def get_all_orders(self):
        return self.find_element(self.ALL_ORDERS).text
    
    @allure.step('Получение всех заказов за сегодня до оформления')
    def get_all_orders_today(self):
        return self.find_element(self.ORDER_TODAY).text
    
    @allure.step('Получение заказа в работе')
    def get_all_order_in_work(self):
        return self.find_element(self.IN_WORK_ORDER).text
    
    @allure.step('Проверка изменения счетчика всех заказов')
    def check_all_order(self, orders):
        def get_number(text):
            return int(''.join(filter(str.isdigit, text)))

        current = get_number(orders)
        expected = current + 1
        
        # Добавляем повторные попытки с задержкой
        max_attempts = 5
        for attempt in range(max_attempts):
            actual = get_number(self.get_all_orders())
            
            if actual == expected:
                print(f"Счетчик заказов обновился: {current} -> {actual}")
                return True
            
            print(f"Попытка {attempt + 1}: счетчик не обновился. Ожидалось: {expected}, текущее: {actual}")
            if attempt < max_attempts - 1:
                time.sleep(2)  # Ждем 2 секунды перед следующей попыткой
        
        # Если после всех попыток счетчик не обновился
        assert actual == expected, f"Счетчик заказов не обновился: ожидалось {expected}, но получили {actual}"

    @allure.step('Проверка изменения счетчика заказов за сегодня')
    def check_all_order_today(self, orders):
        def get_number(text):
            return int(''.join(filter(str.isdigit, text)))

        current = get_number(orders)
        expected = current + 1
        
        # Добавляем повторные попытки с задержкой
        max_attempts = 5
        for attempt in range(max_attempts):
            actual = get_number(self.get_all_orders_today())
            
            if actual == expected:
                print(f"Счетчик заказов за сегодня обновился: {current} -> {actual}")
                return True
            
            print(f"Попытка {attempt + 1}: счетчик за сегодня не обновился. Ожидалось: {expected}, текущее: {actual}")
            if attempt < max_attempts - 1:
                time.sleep(2)  # Ждем 2 секунды перед следующей попыткой
        
        # Если после всех попыток счетчик не обновился
        assert actual == expected, f"Счетчик заказов за сегодня не обновился: ожидалось {expected}, но получили {actual}"

    @allure.step('Проверка номера заказа в работе')
    def check_order_in_work(self, number):
        number_in_work = self.get_all_order_in_work()
        number_in_work = f'#{number_in_work}'
        print(f"DEBUG: Comparing order numbers - Expected: {number}, Actual: {number_in_work}")
        assert number == number_in_work, f"Order numbers don't match: {number} != {number_in_work}"
    
    @allure.step('Проверка наличия заказа в ленте заказов')
    def check_order_in_list(self, order_number):
        # Локатор для поиска заказа по номеру в ленте
        order_locator = (By.XPATH, f"//p[contains(text(), '{order_number}')]")
    
        try:
            # Ждем появления заказа с нашим номером
            order_element = self.waiting_visibility_element(order_locator, timeout=15)
            print(f"Заказ {order_number} найден в ленте заказов")
            return True
        except:
            print(f"Заказ {order_number} не найден в ленте заказов")
            return False
