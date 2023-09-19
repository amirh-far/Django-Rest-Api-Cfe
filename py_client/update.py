import requests


endpoint = "http://localhost:8000/api/products/3/update"

data = {
    "title": "Yep. Now we're talking",
    "price": 149.99,
}
get_response = requests.put(endpoint, json=data)
print(get_response.text )
print(get_response.status_code)

# print(get_response.json) 