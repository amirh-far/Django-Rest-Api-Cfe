import requests
from getpass import getpass
endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?\n")
password = getpass("What is your password\n")
auth_response = requests.post(endpoint, json={"username": username, "password": password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {
        "Authorization" : f"Bearer {token}" # The deafult string starts with f"Token ...""
    }
    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.text )
    print(get_response.status_code)
    data = get_response.json()
    next_url = data["next"]
    results = data["results"]
    print("next_url", next_url)
    print(results)
# print(get_response.json) 