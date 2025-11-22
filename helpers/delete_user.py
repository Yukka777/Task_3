import allure

from config import Config
from path import Path
from api_requests.requests import Request



# метод удаления пользователя
def delete_user(token):

    with allure.step("отправляем запрос на удаление пользователя"): 
        client = Request(Config.URL)
        response = client.delete(path=Path.DELETE_USER, auth_token=token)
        assert response.status_code == 202
