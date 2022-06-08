import requests
from get_auth_token import get_auth_token
import json

token = get_auth_token("romnegrillo", "romrom")
user_ids = [1,2,3,4]

if token is not None:
    endpoint = f"http://localhost:8000/users/delete/multiple/"
    headers = {
        "Authorization": f"Token {token}"
    }
    json = {
        "user_ids": user_ids
    }

    response = requests.post(endpoint, headers=headers, json=json)
    print(f"Status code: {response.status_code}")
    print(endpoint)

    if response.status_code == 200:
        print(response.json())
    else:
        print("User does not exist.")

else:
    print("Wrong credentials.")
