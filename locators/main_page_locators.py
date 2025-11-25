from selenium.webdriver.common.by import By


class MainPageLocators:
    # Элементы навигации в верхней части страницы
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[text() = "Конструктор"]')
    BUTTON_ORDER_FEED_IN_HEADER = (By.XPATH, "//p[text()='Лента Заказов']")
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Основной заголовок страницы конструктора
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

    # Элементы модального окна с информацией об ингредиенте
    MODAL_OF_INGREDIENT = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    BUTTON_CLOSE_MODAL = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

    # Фон затемнения для модальных окон
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    # Изображение компонента бургера в списке ингредиентов
    BURGER_INGREDIENT = (By.XPATH, './/img[@alt="Флюоресцентная булка R2-D3"]')
    # Область для добавления компонентов бургера
    BASKET_FOR_INGREDIENTS = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__')]")

    # Индикатор количества добавленных ингредиентов
    COUNT_OF_INGREDIENTS = (By.XPATH, ".//ul[contains(@class, 'BurgerIngredients_ingredients__')]//p[contains(text(),'Флюоресцентная булка R2-D3')]/following-sibling::div//p[contains(@class, 'counter')]")

    # Элементы управления процессом заказа
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    BUTTON_LOGIN_TO_ORDER = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")

    # Элементы связанные с оформлением и подтверждением заказа                                                    
    ORDER_MODAL = (By.XPATH, ".//div[contains(@class, 'Modal_modal__container')]")
    ORDER_NUMBER_LOADING = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    ORDER_NUMBER_CONFIRM = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    BUTTON_CLOSE_CONFIRMATION = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button[contains(@class, 'Modal_modal__close')]")
