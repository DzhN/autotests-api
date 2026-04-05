from __future__ import annotations

from pydantic import BaseModel, Field, ConfigDict, EmailStr

from tools.fakers import fake


class ShortUserShema(BaseModel):
    """
    Краткое описание структуры пользователя.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    email: EmailStr = Field(default_factory=fake.email)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)

class ExtendedUserSchema(ShortUserShema):
    """
    Полное описание структуры пользователя.
    """
    id: str

class CreateUserRequestSchema(ShortUserShema):
    """
    Описание структуры запроса на создание пользователя.
    """
    password: str = Field(default_factory=fake.password)

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: ExtendedUserSchema

class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str | None = Field(alias="middleName", default_factory=fake.middle_name)

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