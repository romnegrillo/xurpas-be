import requests
from get_auth_token import get_auth_token
import json

token = get_auth_token("romnegrillo", "romrom")

if token is not None:
    endpoint = "http://localhost:8000/users/create/"
    headers = {
        "Authorization": f"Token {token}"
    }

    json = {
        "username": "scriptuser1",
        "firstname": "Script",
        "lastname": "User",
        "email": "scriptuser@example.org",
        "address": "Sample address",
        "post_code": "1234567890",
        "contact_phone_number": "1234567890"
    }

    response = requests.post(endpoint, headers=headers, json=json)
    print(f"Status code: {response.status_code}")
    print(endpoint)

    try:
        print(response.json())
    except requests.JSONDecodeError:
        pass

else:
    print("Wrong credentials.") 
