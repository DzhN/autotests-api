from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_shema
from tools.fakers import fake

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="testPass",
    last_name= "Dzhanaev",
    first_name= "Nickolai",
    middle_name= "Johnson"
)

create_user_response = public_user_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

private_user_client = get_private_users_client(authentication_user)
get_user_api_response = private_user_client.get_user_api(create_user_response.user.id)
get_user_response_shema = GetUserResponseSchema.model_json_schema()
validate_json_shema(get_user_api_response.json(), get_user_response_shema)