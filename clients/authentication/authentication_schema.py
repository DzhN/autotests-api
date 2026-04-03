from pydantic import BaseModel, Field

class TokenShema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestShema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class LoginResponseShema(BaseModel):
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenShema

class RefreshRequestShema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken")