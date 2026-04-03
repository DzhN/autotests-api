from httpx import Response

from clients.api_client import ApiClient
from clients.authentication.authentication_schema import LoginRequestShema, LoginResponseShema, RefreshRequestShema

from clients.public_http_builder import get_public_http_client

class AuthentificationApiClient(ApiClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: LoginRequestShema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/authentication/login",
            # Сериализуем модель в словарь с использованием alias
            json=request.model_dump(by_alias=True)
        )

    def refresh_api(self, request: RefreshRequestShema) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/authentication/refresh",
            # Сериализуем модель в словарь с использованием alias
            json=request.model_dump(by_alias=True)
        )

    def login(self, request: LoginRequestShema) -> LoginResponseShema:
        response = self.login_api(request)
        # Инициализируем модель через валидацию JSON строки
        return LoginResponseShema.model_validate_json(response.text)

# Добавляем builder для PublicUsersClient
def get_authentication_client() -> AuthentificationApiClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthentificationApiClient(client=get_public_http_client())