from http import HTTPStatus

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_shema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
import pytest


@pytest.mark.regression
@pytest.mark.users
def test_create_user(func_public_user_client):
    # Формируем тело запроса на создание пользователя
    request = CreateUserRequestSchema()
    response = func_public_user_client.create_user_api(request)
    # Инициализируем модель ответа на основе полученного JSON в ответе
    # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    # Проверяем статус-код ответа
    assert_status_code(response.status_code, HTTPStatus.OK)
    # Используем функцию для проверки ответа создания юзера
    assert_create_user_response(request, response_data)
    
    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_shema(response.json(), response_data.model_json_schema())

@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(func_user, private_users_client):
    response_user_me = private_users_client.get_user_me_api()
    response_user_me_data = GetUserResponseSchema.model_validate_json(response_user_me.text)
    assert_status_code(response_user_me.status_code, HTTPStatus.OK)
    assert_get_user_response(response_user_me_data.user, func_user.response.user)