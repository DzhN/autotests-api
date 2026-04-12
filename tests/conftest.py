import pytest
from pydantic import BaseModel

from clients.authentication.authentication_client import AuthentificationClient, get_authentication_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    """
    Модель для агрегации возвращаемых данных фикстурой function_user
    """

    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(
            email=self.request.email,
            password=self.request.password
        )


@pytest.fixture
def func_authentification_client() -> AuthentificationClient:
     return get_authentication_client()

@pytest.fixture
def func_public_user_client() -> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture
def func_user(func_public_user_client):
    request = CreateUserRequestSchema()
    response = func_public_user_client.create_user(request)
    return UserFixture(request=request, response=response)

@pytest.fixture
def private_users_client(func_user) -> PrivateUsersClient:
    return get_private_users_client(func_user.authentication_user)
