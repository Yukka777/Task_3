import pytest
import tempfile
from selenium import webdriver
from urls import Urls
import requests
from helpers import create_random_email, create_random_password, create_random_name
import urllib3
import warnings
import os
import ssl
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# АГРЕССИВНОЕ ОТКЛЮЧЕНИЕ SSL ПРОВЕРОК
os.environ['PYTHONHTTPSVERIFY'] = '0'
os.environ['CURL_CA_BUNDLE'] = ''

# Отключить все SSL предупреждения
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore", category=InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Отключить SSL проверку на уровне контекста
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Создать сессию с отключенной SSL проверкой
session = requests.Session()
session.verify = False
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('http://', adapter)
session.mount('https://', adapter)

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    """Фикстура для инициализации веб-драйвера с поддержкой Chrome и Firefox
    
    Особенности:
    - Параметризация для тестирования в обоих браузерах
    - Уникальная user-data-dir для Chrome для избежания конфликтов
    - Автоматическое закрытие драйвера после тестов
    """
    browser_name = request.param
    driver = None
    
    try:
        if browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--width=1920')
            options.add_argument('--height=1080')
            # ОТКЛЮЧЕНИЕ ПРОКСИ ДЛЯ FIREFOX
            options.set_preference('network.proxy.type', 0)
            options.set_preference('network.proxy.socks_remote_dns', False)
            options.set_preference('network.http.use-cache', True)
            options.set_preference('browser.cache.disk.enable', True)
            options.set_preference('browser.cache.memory.enable', True)
            options.set_preference('browser.cache.offline.enable', True)
            driver = webdriver.Firefox(options=options)
            
        elif browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            # ОТКЛЮЧЕНИЕ ПРОКСИ ДЛЯ CHROME
            options.add_argument("--no-proxy-server")
            options.add_argument("--proxy-server='direct://'")
            options.add_argument("--proxy-bypass-list=*")
            options.add_argument("--ignore-certificate-errors")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            
            temp_dir = tempfile.mkdtemp()
            options.add_argument(f"--user-data-dir={temp_dir}")
            driver = webdriver.Chrome(options=options)
        
        # УВЕЛИЧИВАЕМ ТАЙМАУТЫ
        driver.implicitly_wait(30)
        driver.set_page_load_timeout(30)
        driver.set_script_timeout(30)
        
        # ЯВНОЕ ОТКЛЮЧЕНИЕ ПРОКСИ НА УРОВНЕ DRIVER
        try:
            driver.command_executor._proxy = None
        except:
            pass
            
        driver.get(Urls.BASE_URL)
        yield driver
        
    except Exception as e:
        print(f"Ошибка при инициализации драйвера {browser_name}: {e}")
        if driver:
            driver.quit()
        raise
        
    finally:
        if driver:
            driver.quit()

@pytest.fixture
def create_new_user_and_delete():
    """Фикстура для создания временного пользователя с автоматическим удалением"""
    # Генерация случайных учетных данных
    payload_cred = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_name()
    }
    
    # Используем сессию с отключенной SSL проверкой
    response = session.post(Urls.USER_REGISTER, data=payload_cred)
    response_body = response.json()

    # Возврат данных для использования в тестах
    yield payload_cred, response_body

    # Автоматическое удаление пользователя после теста
    access_token = response_body['accessToken']
    session.delete(Urls.USER_DELETE, headers={'Authorization': access_token})
