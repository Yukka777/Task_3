import allure

from config import Config
from path import Path
from api_requests.requests import Request



# метод регистрации нового пользователя возвращает token после успешной регистрации
def register_new_user_and_return_token(user_map):

    with allure.step("собираем тело запроса"):
        user_data = user_map
        payload = {
            "email": user_data["email"],
            "password": user_data["password"],
            "name": user_data["name"]
        }

    with allure.step("отправляем запрос на регистрацию пользвателя и сохраняем ответ в переменную response"): 
        client = Request(Config.URL)
        response = client.post(path=Path.REGISTER_USER, json=payload)

        if response.status_code == 200:
            token = response.json()["accessToken"]

    return token 
