from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        """Инициализация основного класса страницы с веб-драйвером"""
        self.driver = driver


    @allure.step('Выполнить скрипт JavaScript')
    def execute_javascript(self, script, *args):
        """Запуск JavaScript кода в контексте текущей страницы"""
        return self.driver.execute_script(script, *args)
    

    @allure.step('Создать последовательность действий')
    def create_action_chains(self):
        """Создание объекта для выполнения последовательных действий"""
        return ActionChains(self.driver)
        

    @allure.step('Ожидать появления элемента')
    def wait_visibility_of_element(self, locator, timeout=20):
        """Ожидание отображения элемента в течение указанного времени"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    
    @allure.step('Выполнить клик по элементу')
    def click_on_element(self, locator):
        """Активация элемента с обработкой случаев перекрытия"""
        try:
            target = self.check_element_is_clickable(locator)
            target.click()
        except ElementClickInterceptedException:
            # Альтернативный метод активации через JavaScript
            element = self.find_element_with_wait(locator)
            self.execute_javascript("arguments[0].click();", element)


    @allure.step('Найти элемент с ожиданием')
    def find_element_with_wait(self, locator, timeout=20):
        """Поиск элемента с ожиданием его появления в DOM"""
        return self.wait_visibility_of_element(locator, timeout)
    
    
    @allure.step('Заполнить поле ввода')
    def send_keys_to_input(self, locator, keys):
        """Ввод данных в поле с предварительной очисткой содержимого"""
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(keys)


    @allure.step('Переместить элемент')
    def drag_and_drop_element(self, source_element, target_element):
        """Выполнение операции перетаскивания между элементами"""
        try:
            # Основной метод для Chrome
            ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
        except:
            # Резервный метод для Firefox
            ActionChains(self.driver).click_and_hold(source_element)\
                .move_to_element(target_element)\
                .release()\
                .perform()
        # Ожидание завершения визуальных изменений
        self.wait_for_ui_update()


    @allure.step('Получить текстовое содержимое элемента')
    def get_text_on_element(self, locator):
        """Извлечение текстового содержимого из указанного элемента"""
        element = self.find_element_with_wait(locator)
        return element.text
    
    
    @allure.step('Проверить видимость элемента')
    def check_displaying_of_element(self, locator, timeout=10):
        """Проверка отображения элемента в пользовательском интерфейсе"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except:
            return False
        
        
    @allure.step('Проверить отсутствие элемента')
    def check_not_displaying_of_element(self, locator, timeout=10):
        """Проверка отсутствия элемента в видимой области"""
        try:
            self.wait_for_closing_of_element(locator, timeout)
            return True
        except:
            return False
        

    @allure.step('Ожидать скрытия элемента')
    def wait_for_closing_of_element(self, locator, timeout=20):
        """Ожидание полного исчезновения элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    
    
    @allure.step('Проверить доступность элемента для клика')
    def check_element_is_clickable(self, locator, timeout=20):
        """Проверка возможности взаимодействия с элементом"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    
    @allure.step('Ожидать изменения текста элемента')
    def wait_for_element_to_change_text(self, locator, old_text, timeout=30):
        """Ожидание смены текстового содержимого элемента"""
        return WebDriverWait(self.driver, timeout).until_not(
            EC.text_to_be_present_in_element(locator, old_text)
        )
    
    
    @allure.step('Ожидать обновления интерфейса')
    def wait_for_ui_update(self, timeout=5):
        """Ожидание завершения всех визуальных изменений"""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

        
    @allure.step('Ожидать появления корректного текста')
    def wait_for_element_to_have_valid_text(self, locator, timeout=30):
        """Ожидание появления осмысленного текстового содержимого"""
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*locator).text and 
                          driver.find_element(*locator).text.strip() and 
                          not driver.find_element(*locator).text.isspace())
    
    
    @allure.step('Выполнить перетаскивание через JavaScript')
    def execute_javascript_drag_and_drop(self, source_element, target_element):
        """Выполнение drag-and-drop через JavaScript"""
        self.execute_javascript("""
            var source = arguments[0];
            var target = arguments[1];
            
            var dragStart = new Event('dragstart', { bubbles: true });
            var dragOver = new Event('dragover', { bubbles: true });
            var drop = new Event('drop', { bubbles: true });
            
            source.dispatchEvent(dragStart);
            target.dispatchEvent(dragOver);
            target.dispatchEvent(drop);
        """, source_element, target_element)
