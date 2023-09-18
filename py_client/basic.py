import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query": "Hello world"}) # HTTP request
print(get_response.text) # Print raw text response

# HTTP Request -> HTML
# REST API Request -> JSON
# JavaScript Object Notation ~ Python Dict
print(get_response.json())