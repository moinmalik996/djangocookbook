import requests

# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbin.org/anything'

endpoint = 'http://localhost:8000/api/'



params = {
    'item':12
}

response = requests.get(endpoint)

# print(response.status_code) #print whole response
# print(response.text)
print(response.json())

# print(response.json()['message'])

