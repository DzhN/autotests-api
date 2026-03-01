import httpx
from tools.fakers import get_random_email

url = "http://localhost:8000"
body_create_user = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

client = httpx.Client()
response_create_user = client.post(f"{url}/api/v1/users", json=body_create_user)
response_create_user_data = (response_create_user.json())

print("create_user.status_code", response_create_user.status_code)

body_login = {
  "email": body_create_user["email"],
  "password": body_create_user["password"]
}
response_login = client.post(f"{url}/api/v1/authentication/login", json=body_login)
response_login_data = response_login.json()

print("login.status_code", response_login.status_code)
print(response_login_data)

headers_update_user = {
  "Authorization": f"Bearer {response_login_data['token']['accessToken']}"
}
body_update_user = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

response_update_user = httpx.patch(f"{url}/api/v1/users/{response_create_user_data['user']['id']}",
                                   headers=headers_update_user, json=body_update_user)

print(response_update_user.status_code)
