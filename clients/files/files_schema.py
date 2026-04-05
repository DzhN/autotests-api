from pydantic import BaseModel, HttpUrl, Field

from tools.fakers import fake


# Добавили описание структуры файла
class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    # Директорию оставляем статичной, чтобы все тестовые файлы на сервере попадали в одну папку
    directory: str = Field(default="tests")
    upload_file: str


# Добавили описание структуры ответа на создание файла
class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema
