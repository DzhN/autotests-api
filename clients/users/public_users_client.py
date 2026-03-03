from typing import TypedDict

from clients.api_client import ApiClient

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(ApiClient):
    def create_user_api(self, url, request: CreateUserRequestDict):
        """
        Метод для создания пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url, json=request)
