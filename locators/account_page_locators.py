from selenium.webdriver.common.by import By

class AccountPageLocators:
    """Локаторы элементов интерфейса для форм входа и профиля пользователя"""
    
    # Форма входа
    AUTH_FORM = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")
    
    # Поля для ввода учетных данных
    INPUT_EMAIL = (By.XPATH, ".//input[@name = 'name']")
    INPUT_PASSWORD = (By.XPATH, ".//input[@name = 'Пароль']")
    
    # Элементы управления аутентификацией
    BUTTON_LOGIN = (By.XPATH, "//button[text() = 'Войти']")
    BUTTON_REGISTER = (By.XPATH, "//a[text() = 'Зарегистрироваться']")
    BUTTON_RECOVER = (By.XPATH, "//a[text() = 'Восстановить пароль']")
    
    # Заголовок раздела авторизации
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    
    # Элементы управления профилем пользователя
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(), 'Выход')]")
