import requests
from get_auth_token import get_auth_token
import json

token = get_auth_token("romnegrillo", "romrom")
user_id = 1

if token is not None:
    endpoint = f"http://localhost:8000/users/update/{user_id}/"
    headers = {
        "Authorization": f"Token {token}"
    }
    json = {
        "username": "updaterUser",
        "firstname": "Script Updated",
        "lastname": "User",
        "email": "scriptuser@example.org",
        "address": "Sample address",
        "post_code": "1234567890",
        "contact_phone_number": "1234567890"
    }
    response = requests.put(endpoint, headers=headers, json=json)
    print(f"Status code: {response.status_code}")
    print(endpoint)

    if response.status_code == 200:
        print(response.json())
    else:
        print("User does not exist.")

else:
    print("Wrong credentials.")
