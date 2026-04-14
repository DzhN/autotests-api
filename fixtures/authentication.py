import pytest

from clients.authentication.authentication_client import AuthentificationClient, get_authentication_client

@pytest.fixture
def func_authentication_client() -> AuthentificationClient:
    return get_authentication_client()