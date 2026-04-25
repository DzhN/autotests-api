import pytest
from pydantic import BaseModel
from typing_extensions import ClassVar

from clients.courses.courses_client import get_courses_client, CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture, func_user

class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

@pytest.fixture
def courses_client(func_user: UserFixture) -> CoursesClient:
    return get_courses_client(func_user.authentication_user)

@pytest.fixture
def func_course(
        courses_client: CoursesClient,
        func_user: UserFixture,
        func_file:FileFixture
) -> CourseFixture:
    request = CreateCourseRequestSchema(
        preview_file_id=func_file.response.file.id,
        created_by_user_id=func_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)
