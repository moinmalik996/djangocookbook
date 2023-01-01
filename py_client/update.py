import requests


endpoint = 'http://localhost:8000/api/product/1/update/'



payload = {
    'title' : "Updated the title",
    'content':'this is our new product',
    'price': 50.00
}

response = requests.put(endpoint, json=payload)

print(response.json())
