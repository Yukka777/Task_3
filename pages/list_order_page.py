import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class IngredientPage(BasePage):
    INGREDIENT_TITLE_TEXT = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')][1]")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Ожидание появления текста Детали ингредиента')
    def check_ingredient_form_title(self):
        assert self.waiting_text_in_element(self.INGREDIENT_TITLE_TEXT, "Детали ингредиента")

    @allure.step('Закрыть форму ингредиента')
    def close_ingredient_form(self):
        self.waiting_clickable(self.CLOSE_BUTTON)
        self.click(self.CLOSE_BUTTON)
