from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    """Локаторы для страницы восстановления пароля"""
    
    # Заголовок формы восстановления пароля
    RECOVERY_FORM = (By.XPATH, "//h2[text()='Восстановление пароля']")
    
    # Поле для ввода email
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    
    # Кнопка восстановления пароля
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    
    # Ссылка "Войти"
    BACK_TO_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
