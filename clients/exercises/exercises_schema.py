from pydantic import BaseModel, Field, ConfigDict

class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий для определенного курса.
    """
    courseId: str

class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка заданий для определенного курса.
    """
    exercises: list[ExerciseSchema]

class GetExerciseQuerySchema(BaseModel):
    """
    Получение информации о задании по exercise_id.
    """
    exercise_id: str

class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение информации о задании по exercise_id.
    """
    exercise: ExerciseSchema

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания для определенного курса.
    """

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание задания для определенного курса.
    """
    exercise: ExerciseSchema

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление списка заданий для определенного курса.
    """
    title: str = Field(default=None)
    max_score: int = Field(alias="maxScore", default=None)
    min_score: int = Field(alias="minScore", default=None)
    order_index: int = Field(alias="orderIndex", default=None)
    description: str = Field(default=None)
    estimated_time: str = Field(alias="estimatedTime", default=None)

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на обновление списка заданий для определенного курса.
    """
    exercise: ExerciseSchema

"""
Описание структуры ответа на удаление задания.
"""
DeleteExerciseResponseSchema = str