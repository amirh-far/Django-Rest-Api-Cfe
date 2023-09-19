import requests


endpoint = "http://localhost:8000/api/products/"
data = {
    "title" : "New title content",
    "price" : "12.99"
}
get_response = requests.post(endpoint, json=data)
print(get_response.text )
print(get_response.status_code)

# print(get_response.json) 