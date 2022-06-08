import requests
from get_auth_token import get_auth_token
import json

token = get_auth_token("romnegrillo", "romrom")
user_id = 3

if token is not None:
    endpoint = f"http://localhost:8000/users/retrieve/{user_id}/"
    headers = {
        "Authorization": f"Token {token}"
    }
    response = requests.get(endpoint, headers=headers)
    print(f"Status code: {response.status_code}")
    print(endpoint)

    if response.status_code == 200:
        print(response.json())
    else:
        print("User does not exist.")

else:
    print("Wrong credentials.") 
