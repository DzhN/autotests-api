import pytest
from _pytest.fixtures import SubRequest


@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
# Фикстура будет возвращать три разных хоста
# Соответственно все автотесты использующие данную фикстуру будут запускаться три раза
def host(request: SubRequest) -> str:
    # Внутри атрибута param находится одно из значений "https://dev.company.com",
    # "https://stable.company.com", "https://prod.company.com"
    return request.param


# В самом автотесте уже не нужно добавлять параметризацию, он будет автоматически параметризован из фикстуры
def test_host(host: str):
    # Используем фикстуру в автотесте, она вернет нам хост в виде строки
    print(f"Running test on host: {host}")

@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def test_multiplication_of_numbers(os: str, host: str):
    assert len(os + host) > 0

# Для тестовых классов параметризация указывается для самого класса
@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    # Параметр "user" передается в качестве аргумента в каждый тестовый метод класса
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    # Аналогично тут передается "user"
    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")