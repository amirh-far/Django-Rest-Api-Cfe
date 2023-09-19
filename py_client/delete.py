import requests

input_id = input("What's the product id you want to delete?")

try:
    input_id = int(input_id)
except:
    print(f"{input_id} is not valid")
    input_id = None


if input_id:
    endpoint = f"http://localhost:8000/api/products/{input_id}/delete"
    get_response = requests.delete(endpoint, json={"id" : input_id})
    print(get_response.text )
    print(get_response.status_code)

# print(get_response.json) 