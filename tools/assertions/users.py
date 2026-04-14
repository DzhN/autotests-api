from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, ExtendedUserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")

def assert_user(response_get_user: ExtendedUserSchema, response_create_user: ExtendedUserSchema):
    """
    Проверяет, что ответ на получение данных пользователя соответствует данным, полученным
    при создании пользователя

    :param response_get_user: Ответ на получение данных
    :param response_create_user: Ответ на создание пользователя
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    print("response_get_user: ", response_get_user)

    assert_equal(response_get_user.email, response_create_user.email, "email")
    assert_equal(response_get_user.first_name, response_create_user.first_name, "first_name")
    assert_equal(response_get_user.last_name, response_create_user.last_name, "last_name")
    assert_equal(response_get_user.middle_name, response_create_user.middle_name, "middle_name")
    assert_equal(response_get_user.id, response_create_user.id, "id")

def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    assert_user(get_user_response.user, create_user_response.user)
