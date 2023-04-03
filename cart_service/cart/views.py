from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from cart.models import CartItem
from product_update.views import update_product_quantity, get_product
from django.views.decorators.http import require_http_methods


def get_cart_item(cart_id, product_id):
    products = CartItem.objects.filter(cart_id=cart_id, product_id=product_id)
    return products.first()


def data_insert(cart_id, price, quantity, product_id):
    cart_item = CartItem(cart_id=cart_id, price=price, quantity=quantity, product_id=product_id)
    cart_item.save()
    return 1


@csrf_exempt
def handle_request(request, cart_id):
    if request.method == 'POST':
        return add_to_cart(request, cart_id)
    elif request.method == 'GET':
        return get_cart_items(request, cart_id)
    elif request.method == 'DELETE':
        return deleteCartItem(request,cart_id)
    elif request.method == 'PUT':
        return update_cart(request,cart_id)


@csrf_exempt
def add_to_cart(request, cart_id):
    if request.method == 'POST':
        resp = {}
        if 'application/json' in request.META['CONTENT_TYPE']:
            val = json.loads(request.body)

            quantity = val.get('quantity')
            price = val.get('price')
            product_id = val.get('product_id')

            if cart_id and quantity and price and product_id:
                respdata = get_cart_item(cart_id=cart_id, product_id=product_id)
                if respdata:
                    respdata.quantity += quantity
                    # update_product_quantity(product_id, quantity)
                    respdata.save()
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['message'] = 'Them Thanh Cong'
                else:
                    if data_insert(cart_id, price, quantity, product_id):
                        resp['status'] = 'Success'
                        resp['status_code'] = '200'
                        resp['message'] = 'Them Thanh Cong'
                    else:
                        resp['status'] = 'Failed'
                        resp['status_code'] = '400'
                        resp['message'] = 'Them That Bai'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Thieu Truong Thong Tin'
        return HttpResponse(json.dumps(resp), content_type='application/json')


@csrf_exempt
def get_cart_items(request, cart_id):
    data = []
    resp = {}

    # This will fetch the data from the database.
    cart_items = CartItem.objects.filter(cart_id=cart_id)

    total_items = len(cart_items)
    total_price = 0
    for tbl_value in cart_items.values():
        respond = get_product(tbl_value['product_id'])
        del tbl_value['product_id']
        tbl_value['product'] = respond['product']
        total_price += tbl_value['price']*tbl_value['quantity']
        data.append(tbl_value)
    resp['total_items'] = total_items
    resp['total_price'] = total_price

    # If data is available then it returns the data.
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Khong Co Du Lieu'
    return HttpResponse(json.dumps(resp), content_type='application/json')


@csrf_exempt
def deleteCartItem(request, cart_id):
    resp = {}
    val = json.loads(request.body)
    product_id = val['product_id']
    respdata = get_cart_item(cart_id,product_id)

    if respdata is None:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Khong Co Du Lieu'
    else:

        respdata.delete()
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'Xoa Thanh Cong'

    return HttpResponse(json.dumps(resp), content_type='application/json')


@csrf_exempt
def update_cart(request, cart_id):
    resp = {}
    val = json.loads(request.body)
    product_id = val['product_id']
    quantity = val['quantity']
    price = val['price']
    respdata = get_cart_item(cart_id,product_id)

    if respdata is None:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Khong Co Du Lieu'
    else:

        respdata.quantity = quantity
        if quantity > 0 :
            respdata.save()
        else:
            respdata.delete()
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'sua thanh cong'

    return HttpResponse(json.dumps(resp), content_type='application/json')


