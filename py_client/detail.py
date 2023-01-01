import requests

input_methods = [1, 2, 3]
product_id = input('Enter the product ID : ')

try:
    print('1 For DETAIL')
    print('2 For UPDATE')
    print('3 For DELETE')
    action = int(input('ENTER YOUR CHOICE : '))

    while (action not in input_methods) or action in ['', None]:
        print('1 For DETAIL')
        print('2 For UPDATE')
        print('3 For DELETE')
        action = int(input('ENTER YOUR CHOICE : '))
        product_id = int(product_id)
except:
    print(f"Invalid Product ID : {product_id}")
    product_id = None


endpoint = f'http://localhost:8000/api/product/{product_id}/'


if product_id:

    if action == 1:
        response = requests.get(endpoint)

    if action == 2:

        payload = {
            'title':'Update Title',
            'content':'Update Content',
            'price':'33.00'
        }
        response = requests.put(endpoint, payload=payload)

    if action == 3:
        response = requests.delete(endpoint)

    print(response.status_code, response.status_code==204)
