import httpx

url = "http://localhost:8000"
body = {
    "email": "user@example.com",
    "password": "string"
}

client = httpx.Client()
auth_response = client.post(f"{url}/api/v1/authentication/login", json=body)

auth_response_data = auth_response.json()
access_token = auth_response_data["token"]["accessToken"]

print(auth_response.status_code)
print(auth_response_data)

headers = {"Authorization": f"Bearer {access_token}"}
user_response = client.get(f"{url}/api/v1/users/me", headers=headers)

print(user_response.status_code)
print(user_response.json())