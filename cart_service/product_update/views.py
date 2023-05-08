from django.shortcuts import render

import requests
import json


# Create your views here.

def update_product_quantity(product_id, quantity):
    url = f'http://127.0.0.1:7500/product/{product_id}'

    body = {"quantity": quantity}
    data = json.dumps(body)
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, data=data, headers=headers)
    val = json.loads(response.content.decode('utf-8'))
    return val


def get_product(product_id):
    url = f'http://127.0.0.1:7500/product/{product_id}'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    val = json.loads(response.content.decode('utf-8'))
    return val
