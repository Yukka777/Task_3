import pytest
import tempfile
from selenium import webdriver
from urls import Urls
import requests
import warnings
import os
import ssl
import random
import string

# Деактивация проверок SSL соединения
os.environ['PYTHONHTTPSVERIFY'] = '0'
os.environ['CURL_CA_BUNDLE'] = ''

# Отключение верификации SSL на системном уровне
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Инициализация сессии HTTP с отключенной SSL верификацией
session = requests.Session()
session.verify = False
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Утилиты генерации тестовых данных
def create_random_email():
    """Создание произвольного email адреса для тестирования"""
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=6))
    return f"{username}@{domain}.com"

def create_random_password():
    """Генерация произвольного пароля для тестовых сценариев"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=10))

def create_random_name():
    """Создание произвольного имени пользователя"""
    return ''.join(random.choices(string.ascii_letters, k=10))

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    """Инициализация веб-драйвера с поддержкой нескольких браузеров
    
    Ключевые характеристики:
    - Параметризованный выбор браузера для кроссплатформенного тестирования
    - Изолированные пользовательские профили для Chrome
    - Автоматическое освобождение ресурсов по завершении тестов
    """
    browser_type = request.param
    driver_instance = None
    
    try:
        if browser_type == 'firefox':
            browser_options = webdriver.FirefoxOptions()
            browser_options.add_argument('--width=1920')
            browser_options.add_argument('--height=1080')
            # Деактивация прокси-сервера для Firefox
            browser_options.set_preference('network.proxy.type', 0)
            browser_options.set_preference('network.proxy.socks_remote_dns', False)
            browser_options.set_preference('network.http.use-cache', True)
            browser_options.set_preference('browser.cache.disk.enable', True)
            browser_options.set_preference('browser.cache.memory.enable', True)
            browser_options.set_preference('browser.cache.offline.enable', True)
            driver_instance = webdriver.Firefox(options=browser_options)
            
        elif browser_type == 'chrome':
            browser_options = webdriver.ChromeOptions()
            browser_options.add_argument("--no-sandbox")
            browser_options.add_argument("--disable-dev-shm-usage")
            browser_options.add_argument("--window-size=1920,1080")
            # Деактивация прокси-сервера для Chrome
            browser_options.add_argument("--no-proxy-server")
            browser_options.add_argument("--proxy-server='direct://'")
            browser_options.add_argument("--proxy-bypass-list=*")
            browser_options.add_argument("--ignore-certificate-errors")
            browser_options.add_experimental_option("excludeSwitches", ["enable-logging"])
            
            temporary_directory = tempfile.mkdtemp()
            browser_options.add_argument(f"--user-data-dir={temporary_directory}")
            driver_instance = webdriver.Chrome(options=browser_options)
        
        # Установка увеличенных таймаутов для стабильности тестов
        driver_instance.implicitly_wait(30)
        driver_instance.set_page_load_timeout(30)
        driver_instance.set_script_timeout(30)
        
        # Прямое отключение прокси на уровне драйвера
        try:
            driver_instance.command_executor._proxy = None
        except:
            pass
            
        driver_instance.get(Urls.BASE_URL)
        yield driver_instance
        
    except Exception as error:
        print(f"Ошибка инициализации драйвера {browser_type}: {error}")
        if driver_instance:
            driver_instance.quit()
        raise
        
    finally:
        if driver_instance:
            driver_instance.quit()

@pytest.fixture
def create_new_user_and_delete():
    """Создание временного пользователя с автоматической очисткой после тестов"""
    # Формирование случайных учетных данных
    credentials = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_name()
    }
    
    # Использование сессии с отключенной SSL проверкой
    registration_response = session.post(Urls.USER_REGISTER, data=credentials)
    response_data = registration_response.json()

    # Предоставление данных для тестирования
    yield credentials, response_data

    # Автоматическая очистка тестового пользователя
    auth_token = response_data['accessToken']
    session.delete(Urls.USER_DELETE, headers={'Authorization': auth_token})
