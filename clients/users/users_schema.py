from __future__ import annotations

from pydantic import BaseModel, Field, ConfigDict, EmailStr

class ShortUserShema(BaseModel):
    """
    Краткое описание структуры пользователя.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class ExtendedUserSchema(ShortUserShema):
    """
    Полное описание структуры пользователя.
    """
    id: str

class CreateUserRequestSchema(ShortUserShema):
    """
    Описание структуры запроса на создание пользователя.
    """
    password: str

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: ExtendedUserSchema

class UpdateUserRequestSchema(ShortUserShema):
    """
    Описание структуры запроса на обновление пользователя.
    """

class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления пользователя.
    """
    user: ExtendedUserSchema

class GetUserResponseSchema(BaseModel):
    """
    Описание структуры запроса получения пользователя.
    """
    user: ExtendedUserSchema