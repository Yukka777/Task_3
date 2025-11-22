from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)
    
    def waiting_visibility_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
    
    def waiting_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    def waiting_text_in_element(self, locator, text):
        return WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))

    def waiting_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
    
    def waiting_url(self, url):
        return WebDriverWait(self.driver, 20).until(expected_conditions.url_to_be(url))
    
    def drag_to_locator(self,source_locator, target_locator):
        """Переместить элемент от исходного локатора к целевому"""
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()
