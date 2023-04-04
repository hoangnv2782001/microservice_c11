from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from product_model.models import product_details

def insert_shoe(shoe_id,category,name,availability,price,quantity):
    book_data = product_details(product_id=shoe_id,product_name=name,product_category=category,quantity=quantity,availability=availability,price=price)
    book_data.save()
    return 1

@csrf_exempt
def get_product_data(request):
    data = []
    resp = {}
    # pro = product_details(product_id='SP123',product_category='Giay',product_name='giay123',availability='availale',price='100',quantity=100)
    # pro.save()
    # This will fetch the data from the database.
    prodata = product_details.objects.all()
    for tbl_value in prodata.values():
        data.append(tbl_value)
    # If data is available then it returns the data.
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@csrf_exempt
def update_product_quantity(request,product_id):
    resp = {}

    val = json.loads(request.body)
    quantity = val.get('quantity')
    print('hoang dep trrai')

    product = product_details.objects.get(product_id=product_id)
    # product = products.first()

    if product is None:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'product Not Found.'
    else:
        product.quantity = quantity
        product.save()
        resp['status'] = 'Success'
        resp['status_code'] = '200'
    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def get_product(request,product_id):
    resp = {}

    product = product_details.objects.filter(product_id=product_id).values().first()

    if product is None:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'product Not Found.'
    else:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['product'] = product
    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def add_product(request):
    product_id = request.POST.get('id')
    product_name = request.POST.get('name')
    product_category = request.POST.get('category')
    availability = 'available'
    price = request.POST.get('price')
    quantity = request.POST.get('quantity')

    resp = {}
    if product_category  and product_id and product_name and price and quantity :
        ### It will call the store data function.
        respdata = insert_shoe(shoe_id=product_id,name=product_name,price=price,quantity=quantity,availability=availability,category=product_category)
        ### If it returns value then will show success.
        if respdata:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'completed.'
        ### If it is returning null value then it will show failed.
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Please try again.'
        ### If any mandatory field is missing then it will be through a failed message.
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type='application/json')









