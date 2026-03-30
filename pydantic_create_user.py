from pydantic import BaseModel, EmailStr, Field

class ShortUserSchema(BaseModel):
    """
    Описание краткой модели данных пользователя
    """
    email: EmailStr
    last_name:str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class ExtendedUserSchema(ShortUserSchema):
    """
    Описание полной модели данных пользователя: краткая модель + id
    """
    id: str

class CreateUserRequestSchema(ShortUserSchema):
    """
    Описание модели данных запроса на создание пользователя
    """
    password: str

class CreateUserResponseSchema(ExtendedUserSchema):
    """
    Описание модели данных ответа на создание пользователя
    """
    user: ExtendedUserSchema