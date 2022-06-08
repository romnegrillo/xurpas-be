import requests

def get_auth_token(username, password):
    endpoint = "http://localhost:8000/login/"
    json = {
        "username": username,
        "password": password,
    }
    
    response = requests.post(endpoint, json=json)
    print(f"Login status code: {response.status_code}")
    print(endpoint)
    
    if response.status_code == 200:
        return response.json()["token"]
    else:
        return None