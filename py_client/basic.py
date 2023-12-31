import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, params={"abc": 123}, json={"title": "Hello world"}) # HTTP request
print(get_response.text ) # Print raw text response
print(get_response.status_code)

# HTTP Request -> HTML
# REST API Request -> JSON
# JavaScript Object Notation ~ Python Dict
print(get_response.json) 