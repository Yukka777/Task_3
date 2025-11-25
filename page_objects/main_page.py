from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.account_page_locators import AccountPageLocators
import allure

class MainPage(BasePage):
    
    @allure.step('Перейти в личный кабинет через верхнюю панель')
    def click_on_personal_account_in_header(self):
        """Активация элемента навигации для перехода в профиль пользователя"""
        self.click_on_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)

        
    @allure.step('Активировать раздел ленты заказов через верхнюю панель')
    def click_header_feed_button(self):
        """Переход к ленте заказов через элемент навигации в шапке"""
        self.click_on_element(MainPageLocators.BUTTON_ORDER_FEED_IN_HEADER)


    @allure.step('Вернуться в конструктор бургеров')
    def click_on_button_constructor(self):
        """Возврат на основную страницу конструктора через навигацию"""
        self.click_on_element(MainPageLocators.BUTTON_CONSTRUCTOR)


    @allure.step('Получить заголовок конструктора')
    def get_text_on_title_of_constructor(self):
        """Извлечение текста заголовка для подтверждения отображения конструктора"""
        return self.get_text_on_element(MainPageLocators.CONSTRUCTOR_TITLE)
    
    
    @allure.step('Выполнить вход через главную страницу')
    def click_on_button_login_in_main(self):
        """Инициация процесса аутентификации с главной страницы"""
        self.click_on_element(MainPageLocators.BUTTON_LOGIN_TO_ORDER)


    @allure.step('Выбрать компонент бургера')
    def click_on_ingredient(self):
        """Открытие детальной информации о компоненте бургера"""
        self.click_on_element(MainPageLocators.BURGER_INGREDIENT)


    @allure.step('Проверить отображение деталей компонента')
    def check_displaying_of_modal_details(self):
        """Подтверждение отображения окна с характеристиками компонента"""
        return self.check_displaying_of_element(MainPageLocators.MODAL_OF_INGREDIENT)
    
    
    @allure.step('Проверить отсутствие окна деталей компонента')
    def check_not_displaying_of_modal_details(self):
        """Подтверждение закрытия окна с информацией о компоненте"""
        return self.check_not_displaying_of_element(MainPageLocators.MODAL_OF_INGREDIENT)
    

    @allure.step('Закрыть детали компонента"')
    def close_modal(self):
        """Закрытие окна с детальной информацией о компоненте"""
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_MODAL)


    @allure.step('Добавить компонент в заказ')
    def drag_and_drop_ingredient_to_order(self):
        """Перемещение компонента в область сборки бургера"""
        source_element = self.find_element_with_wait(MainPageLocators.BURGER_INGREDIENT)
        target_element = self.find_element_with_wait(MainPageLocators.BASKET_FOR_INGREDIENTS)
        
        # Приоритетная попытка через JavaScript
        try:
            self.execute_javascript_drag_and_drop(source_element, target_element)
        except:
            # Резервный метод через стандартные действия
            self.drag_and_drop_element(source_element, target_element)
        
        # Ожидание применения изменений в интерфейсе
        self.wait_for_ui_update()


    @allure.step('Получить счетчик добавленных компонентов')
    def get_count_of_ingredients(self):
        """Получение количества выбранных компонентов из счетчика"""
        try:
            self.wait_visibility_of_element(MainPageLocators.COUNT_OF_INGREDIENTS, timeout=10)
            count_text = self.get_text_on_element(MainPageLocators.COUNT_OF_INGREDIENTS)
            return count_text if count_text else "0"
        except:
            return "0"
        
        
    @allure.step('Создать заказ')
    def click_on_button_make_order(self):
        """Подтверждение формирования заказа"""
        self.click_on_element(MainPageLocators.BUTTON_MAKE_ORDER)


    @allure.step('Проверить отображение подтверждения заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        """Подтверждение отображения окна с информацией о заказе"""
        return self.check_displaying_of_element(MainPageLocators.ORDER_MODAL)
    
    
    @allure.step('Получить идентификатор заказа')
    def get_number_of_order_in_modal_confirmation(self):
        """Извлечение номера заказа из окна подтверждения"""
        self.wait_visibility_of_element(MainPageLocators.ORDER_NUMBER_CONFIRM, timeout=30)
        self.wait_for_element_to_have_valid_text(MainPageLocators.ORDER_NUMBER_CONFIRM, timeout=30)
        return self.get_text_on_element(MainPageLocators.ORDER_NUMBER_CONFIRM)
    
    
    @allure.step('Закрыть окно подтверждения заказа')
    def click_on_button_close_confirmation_modal(self):
        """Закрытие окна с информацией о заказе"""
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_CONFIRMATION)

        
    @allure.step('Авторизоваться в системе')
    def login(self, email, password):
        """Выполнение полного процесса аутентификации пользователя"""
        self.click_on_element(MainPageLocators.BUTTON_LOGIN_TO_ORDER)
        self.send_keys_to_input(AccountPageLocators.INPUT_EMAIL, email)
        self.send_keys_to_input(AccountPageLocators.INPUT_PASSWORD, password)
        self.click_on_element(AccountPageLocators.BUTTON_LOGIN)
        self.wait_visibility_of_element(MainPageLocators.BUTTON_MAKE_ORDER, timeout=15)


    # Дополнительные методы для повышения надёжности тестов
    @allure.step('Ожидать обработки заказа')
    def wait_for_order_processing(self, timeout=30):
        """Ожидание завершения формирования заказа и получения номера"""
        self.wait_visibility_of_element(MainPageLocators.ORDER_NUMBER_CONFIRM, timeout)


    @allure.step('Проверить доступность компонента')
    def check_ingredient_displayed(self):
        """Подтверждение отображения элемента компонента бургера"""
        return self.check_displaying_of_element(MainPageLocators.BURGER_INGREDIENT)
    

    @allure.step('Проверить отображение области сборки')
    def check_basket_displayed(self):
        """Подтверждение отображения контейнера для компонентов бургера"""
        return self.check_displaying_of_element(MainPageLocators.BASKET_FOR_INGREDIENTS)
    

    @allure.step('Проверить доступность навигации в конструктор')
    def check_constructor_button_displayed(self):
        """Подтверждение отображения элемента возврата в конструктор"""
        return self.check_displaying_of_element(MainPageLocators.BUTTON_CONSTRUCTOR)
