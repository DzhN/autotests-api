from http import HTTPStatus

from clients.authentication.authentication_client import AuthentificationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.private_http_builder import AuthenticationUserSchema
from tests.conftest import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
import pytest


@pytest.mark.regression
@pytest.mark.authentication
def test_login(
        func_user: UserFixture,
        func_authentification_client: AuthentificationClient
        ):
    login_request = LoginRequestSchema(
        email=func_user.request.email,
        password=func_user.request.password
    )
    login_response = func_authentification_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)
