from __future__ import annotations

from typing import TypedDict

from httpx import Response

from clients.api_client import ApiClient

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий для определенного курса.
    """
    courseId: str

class GetExerciseQueryDict(TypedDict):
    """
    Получение информации о задании по exercise_id.
    """
    exercise_id: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание списка заданий для определенного курса.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление списка заданий для определенного курса.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(ApiClient):

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании по exercise_id

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises {exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания задания

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict):
        """
        Метод обновления данных задания.

        :param exercise_id: Идентификатор задания
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str):
        """
        Метод удаления задания

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        self.delete(f"/api/v1/exercises/{exercise_id}")