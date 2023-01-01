import requests


endpoint = 'http://localhost:8000/api/product/1/detail/'


response = requests.get(endpoint)

print(response.json())
