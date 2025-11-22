import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from pages.ingredient_form import IngredientPage
from pages.order_page import OrderPage

class ConstructorPage(BasePage):
    ORDER_MAKE_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    CONSTRUCTOR_TEXT = (By.XPATH, ".//h1[text()='Соберите бургер']")
    BUN = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3' and contains(@class, 'BurgerIngredient_ingredient__text__yp3dH')]")
    BASKET = (By.XPATH, ".//span[text()='Перетяните булочку сюда (верх)']")
    COUNT_BUN = (By.XPATH, ".//p[text()='2']")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")
    SOUCE_SPICY_X = (By.XPATH, ".//p[text()='Соус Spicy-X']")
    SOUCE_SPACE = (By.XPATH, ".//p[text()='Соус фирменный Space Sauce']")
    SOUCE_TRADITIONAL = (By.XPATH, ".//p[text()='Соус традиционный галактический']")
    

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Нажать на Флюоресцентная булка R2-D3')
    def select_ingredient(self):
        self.waiting_clickable(self.BUN)
        self.click(self.BUN)
        return IngredientPage(self.driver)
    
    @allure.step('Добавить Флюоресцентная булка R2-D3 в заказ')
    def drag_to_element(self):
        self.drag_to_locator(self.BUN, self.BASKET)

    @allure.step('Проверка изменения количества у Флюоресцентная булка R2-D3')
    def check_count_buns(self):
        assert self.waiting_text_in_element(self.COUNT_BUN, "2")

    @allure.step('Нажать на кнопку оформления заказа')
    def click_order_button(self):
        self.waiting_clickable(self.ORDER_MAKE_BUTTON)
        self.click(self.ORDER_MAKE_BUTTON)
        return OrderPage(self.driver)
    
    @allure.step('Ожидание появления текста Соберите бургер')
    def check_constructor_text(self):
        assert self.waiting_text_in_element(self.CONSTRUCTOR_TEXT, "Соберите бургер")
