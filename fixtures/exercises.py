import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture


class ExercisesFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercise_client(func_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(func_user.authentication_user)

@pytest.fixture
def func_exercise(exercise_client: ExercisesClient, func_course: CourseFixture, func_user: UserFixture):
    request = CreateExerciseRequestSchema(
        courseId=func_course.response.course.id
    )
    response = exercise_client.create_exercise(request)
    return ExercisesFixture(request=request, response=response)