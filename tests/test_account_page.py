from page_objects.account_page import AccountPage
from page_objects.main_page import MainPage
from conftest import *
import allure


class TestAccountPage:

    @allure.title('Верификация перехода в профиль пользователя')
    @allure.description('''
    Тестирование функциональности доступа к персональному разделу:
    1. Аутентификация в системе с корректными учетными данными
    2. Активация элемента навигации "Личный кабинет" в верхней части интерфейса
    3. Подтверждение успешного перехода в персональный раздел
    4. Верификация наличия элемента выхода из системы как подтверждения авторизации
    ''')
    def test_navigate_to_personal_account_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        
        # Аутентификация в системе с использованием тестовых учетных данных
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        # Переход в персональный раздел через навигационный элемент
        main_page.click_on_personal_account_in_header()
        
        # Подтверждение успешной аутентификации через отображение элемента выхода
        assert account_page.check_logout_button_displayed()
        

    @allure.title('Проверка функционала завершения сеанса"')
    @allure.description('''
    Тестирование процедуры деактивации пользовательской сессии:
    1. Выполнение процедуры аутентификации в системе
    2. Переход в персональный раздел пользователя
    3. Активация элемента завершения сеанса
    4. Подтверждение успешного выхода из системы
    5. Верификация перенаправления на страницу аутентификации
    ''')
    def test_logout_from_profile_page_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        
        # Аутентификация для последующего тестирования выхода из системы
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        # Навигация в персональный раздел с доступом к функции выхода
        main_page.click_on_personal_account_in_header()
        
        # Инициация процедуры завершения пользовательской сессии
        account_page.click_on_logout_button()
        
        # Верификация успешного выхода через отображение элемента регистрации
        account_page.wait_visibility_of_button_register()
        assert account_page.check_displaying_of_button_register()
