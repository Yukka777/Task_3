from selenium.webdriver.common.by import By


class FeedPageLocators:
    # Блок с перечнем заказов
    SECTION_ORDERS_LIST = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')

    # Название раздела ленты заказов
    TITLE_OF_ORDERS_FEED = (By.XPATH, '//h1[text()="Лента заказов"]')

    # Модальное окно деталей заказа
    MODAL_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal")]')

    # Заголовок модального окна с информацией о заказе
    TITLE_OF_MODAL_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal")]//h2')

    # Индикатор общего количества выполненных заказов
    ORDER_COUNTER_BY_ALL_TIME = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    # Индикатор количества заказов за текущие сутки
    ORDER_COUNTER_BY_TODAY = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    # Элементы заказов в статусе выполнения
    ORDER_IN_PROGRESS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]//li") 
    
    # Первая позиция в истории заказов
    ORDER_FIRST_IN_HISTORY = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')][1]")
    
    # Все элементы истории заказов
    ALL_ORDERS_HISTORY = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')
