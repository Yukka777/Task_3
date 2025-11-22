import requests as http_requests

class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def request(self, method, path, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        # Добавьте verify=False для игнорирования SSL ошибок
        response = http_requests.request(method, url, verify=False, **kwargs)
        return response
