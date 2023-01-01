import requests

product_id = input('Enter the product id :  ')

try:
    product_id = int(product_id)
except:
    print(f"Invalid Product ID : {product_id}")
    product_id = None

if product_id:

    endpoint = f'http://localhost:8000/api/product/{product_id}/delete/'

    response = requests.delete(endpoint)

print(response.status_code, response.status_code==204)
