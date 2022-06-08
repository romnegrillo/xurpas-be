import requests
from get_auth_token import get_auth_token
import json

token = get_auth_token("romnegrillo", "romrom")

if token is not None:
    endpoint = "http://localhost:8000/users/list/"
    headers = {
        "Authorization": f"Token {token}"
    }
    response = requests.get(endpoint, headers=headers)
    print(f"Status code: {response.status_code}")
    print(endpoint)

    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2))

else:
    print("Wrong credentials.") 
