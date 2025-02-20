# # tests.py

# import pytest
# from rest_framework import status
# from rest_framework.test import APIClient
# from .models import Product

# @pytest.mark.django_db
# def test_create_product():
#     # Initialize the API client
#     client = APIClient()
    
#     # Define the product data to create
#     product_data = {
#         'name': 'Test Product',
#         'description': 'Test description for the product.',
#         'price': 100.0
#     }
    
#     # Make a POST request to the product creation endpoint
#     response = client.post('/products/', product_data, format='json')
    
#     # Assert that the response status code is 201 (Created)
#     assert response.status_code == status.HTTP_201_CREATED
    
#     # Fetch the created product from the database
#     product = Product.objects.get(id=response.data['id'])
    
#     # Assert that the product data matches what was sent in the request
#     assert product.name == product_data['name']
#     assert product.description == product_data['description']
#     assert product.price == product_data['price']
    
# product/tests.py

import pytest
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product

@pytest.mark.django_db
def test_create_product():
    client = APIClient()
    product_data = {
        'name': 'Test Product',
        'description': 'Test description for the product.',
        'price': 100.0
    }
    response = client.post('/api/products/', product_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
