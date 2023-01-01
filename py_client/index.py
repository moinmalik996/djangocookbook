import requests


endpoint = 'http://localhost:8000/api/product/'



payload = {
    'title' : "perform create method",
    'content':'this is our new product',
    'price': 22.00
}

response = requests.post(endpoint, json=payload)

print(response.json())
