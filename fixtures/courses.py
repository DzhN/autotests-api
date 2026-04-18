import pytest
from pydantic import BaseModel
from typing_extensions import ClassVar

from clients.courses.courses_client import get_courses_client, CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture, func_user

class CoursesFixture(BaseModel):
    request: ClassVar = CreateCourseRequestSchema
    response: ClassVar = CreateCourseResponseSchema

@pytest.fixture
def courses_client(func_user: UserFixture) -> CoursesClient:
    return get_courses_client(func_user.authentication_user)

@pytest.fixture
def func_course(
        courses_client: CoursesClient,
        func_user: UserFixture,
        func_file:FileFixture
) -> CoursesFixture:
    request = CreateCourseRequestSchema(
        previewFileId=func_file.response.file.id,
        createdByUserId=func_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CoursesFixture(request=request, response=response)
