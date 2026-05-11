from http import HTTPStatus

import allure
import pytest

from clients.files.files_schema import GetFileResponseSchema
from fixtures.files import FileFixture
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.errors import assert_create_file_with_empty_filename_response, assert_file_not_found_response
from tools.assertions.files import assert_create_file_response, assert_get_file_response, \
    assert_get_file_with_incorrect_file_id
from clients.errors_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.files
@pytest.mark.regression
@allure.tag(AllureTag.FILES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.FILES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.FILES)
class TestFiles:
    @allure.title("Create file")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file="./testdata/test_document.txt")
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get file")
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_file(self, files_client: FilesClient, func_file: FileFixture):
        response = files_client.get_file_api(func_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, func_file.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Create_file_with_empty_filename")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            filename="",
            upload_file="./testdata/test_document.txt"
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Delete file")
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    def test_delete_file(self, files_client: FilesClient, func_file: FileFixture):
        delete_response = files_client.delete_file_api(func_file.response.file.id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        # Пытаемся получить удаленный файл
        get_response = files_client.get_file_api(func_file.response.file.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)
        # Проверяем, что сервер вернул 404 Not found
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        # Проверяем, что в ответе содержится ошибка Not found
        assert_file_not_found_response(get_response_data)
        # Проверяем, что response соответствует схеме
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    @allure.title("Get_file_with_incorrect_file_id")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient, func_file: FileFixture):
        get_response = files_client.get_file_api("incorrect-file-id")
        get_response_data = ValidationErrorResponseSchema.model_validate_json(get_response.text)
        assert_status_code(get_response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_file_with_incorrect_file_id(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

