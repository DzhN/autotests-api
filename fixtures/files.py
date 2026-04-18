import pytest
from pydantic import BaseModel
from typing_extensions import ClassVar

from clients.files.files_client import get_files_client, FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.users import UserFixture
from fixtures.users import func_user

class FileFixture(BaseModel):
    request: ClassVar = CreateFileRequestSchema
    response: ClassVar = CreateFileResponseSchema


@pytest.fixture
def files_client(func_user: UserFixture):
    return get_files_client(func_user.authentication_user)

@pytest.fixture
def func_file(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file="./testdata/test_document.txt")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)