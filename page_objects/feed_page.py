from page_objects.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
import allure

class FeedPage(BasePage):
    
    @allure.step('Получить заголовок ленты заказов')
    def get_text_on_title_of_orders_list(self):
        """Извлечение текста заголовка для подтверждения отображения страницы"""
        return self.get_text_on_element(FeedPageLocators.TITLE_OF_ORDERS_FEED)

    @allure.step('Получить общее количество выполненных заказов')
    def get_quantity_of_orders(self):
        """Получение значения счетчика выполненных заказов за весь период"""
        self.find_element_with_wait(FeedPageLocators.ORDER_COUNTER_BY_ALL_TIME)
        return self.get_text_on_element(FeedPageLocators.ORDER_COUNTER_BY_ALL_TIME)

    @allure.step('Получить количество заказов за текущий день')
    def get_daily_quantity_of_orders(self):
        """ППолучение значения счетчика заказов выполненных сегодня"""
        self.find_element_with_wait(FeedPageLocators.ORDER_COUNTER_BY_TODAY)
        return self.get_text_on_element(FeedPageLocators.ORDER_COUNTER_BY_TODAY)

    @allure.step('Получить номер заказа в разделе выполняемых"')
    def get_order_number_in_feed_progress_section(self):
        """Извлечение номера заказа из секции текущих выполнений"""
        return self.get_text_on_element(FeedPageLocators.ORDER_IN_PROGRESS)
