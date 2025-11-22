import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class OrderPage(BasePage):
    ORDER_NUMBER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq ')]")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Проверка появления номера заказа после оформления')
    def check_order_number(self):
        assert self.waiting_visibility_element(self.ORDER_NUMBER)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        order_element = self.waiting_visibility_element(self.ORDER_NUMBER)
        order_text = order_element.text.strip()
        
        # Отладочная информация
        print(f"Текст элемента заказа: '{order_text}'")
        
        # Извлекаем номер заказа - ищем последовательность цифр
        import re
        numbers = re.findall(r'\d+', order_text)
        if numbers:
            # Берем первую найденную последовательность цифр (самый длинный номер)
            order_number = max(numbers, key=len)
            return f"#{order_number}"
        
        # Если не нашли цифры, возвращаем как есть
        return order_text
