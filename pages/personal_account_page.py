import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from pages.constructor_page import ConstructorPage
from pages.ingredient_form import IngredientPage
from pages.list_order_page import ListOrderPage
from pages.order_page import OrderPage

class PersonalAccountPage(BasePage):
    ORDER_HISTORY = (By.XPATH, ".//a[text()='История заказов']")
    ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")
    ORDER_MAKE_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    LIST_ORDER_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    ORDER = (By.XPATH, ".//h2[text()='Флюоресцентный бургер'][1]")
    ORDER_WINDOW = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox__1xWdi')]")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Нажать на Личный кабинет')
    def click_personal_account(self):
        self.waiting_clickable(self.ACCOUNT)
        self.click(self.ACCOUNT)

    @allure.step('Нажать на История заказов')
    def click_order_history(self):
        self.waiting_clickable(self.ORDER_HISTORY)
        self.click(self.ORDER_HISTORY)

    @allure.step('Ожидание появления кнопки оформить заказ')
    def check_order_button(self):
        assert self.waiting_visibility_element(self.ORDER_MAKE_BUTTON)

    @allure.step('Проверка перехода на страницу https://stellarburgers.education-services.ru/account/order-history')
    def check_order_history_page(self):
        self.waiting_url("https://stellarburgers.education-services.ru/account/order-history")
        print(self.driver.current_url)
        assert self.driver.current_url == "https://stellarburgers.education-services.ru/account/order-history"

    @allure.step('Нажать на Конструктор')
    def click_constructor_button(self):
        self.waiting_clickable(self.CONSTRUCTOR_BUTTON)
        self.click(self.CONSTRUCTOR_BUTTON)
        return ConstructorPage(self.driver)

    @allure.step('Нажать на Лента заказов')
    def click_list_order_button(self):
        self.waiting_clickable(self.LIST_ORDER_BUTTON)
        self.click(self.LIST_ORDER_BUTTON)
        return ListOrderPage(self.driver)

    @allure.step('Нажать на кнопку выйти')
    def click_exit_button(self):
        self.waiting_clickable(self.EXIT_BUTTON)
        self.click(self.EXIT_BUTTON)

    @allure.step('Проверить номер заказ в списке')
    def check_order_in_list(self, number):
        order_locator_xpath = f".//p[text()='{number}']"
        locator = (By.XPATH, order_locator_xpath)
        print(order_locator_xpath)
        assert self.waiting_visibility_element(locator)

    @allure.step('Нажать на заказ')
    def click_order(self):
        self.waiting_clickable(self.ORDER)
        self.click(self.ORDER)

    @allure.step('Проверка открытия окна с заказом')
    def check_order_window(self):
        assert self.waiting_visibility_element(self.ORDER_WINDOW)

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        return self.find_element(self.ORDER_NUMBER).text
