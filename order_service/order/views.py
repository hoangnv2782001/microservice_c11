import requests
import json

from django.http import HttpResponse
from django.urls import reverse
import urllib
import uuid

boundary = str(uuid.uuid4())

from django.views.decorators.csrf import csrf_exempt

from order.models import Order, OrderItem


#
# # returns the URL from the checkout module for cart
# def get_checkout_url(request):
#     return reverse('checkout')

# def process(request):
#     # Transaction results
#     APPROVED = '1'
#     DECLINED = '2'
#     ERROR = '3'
#     HELD_FOR_REVIEW = '4'
#     postdata = request.POST.copy()
#     card_num = postdata.get('credit_card_number', '')
#     exp_month = postdata.get('credit_card_expire_month', '')
#     exp_year = postdata.get('credit_card_expire_year', '')
#     exp_date = exp_month + exp_year
#     cvv = postdata.get('credit_card_cvv', '')
#     amount = cart.cart_subtotal(request)
#     results = {}
#     response = authnet.do_auth_capture(amount=amount,
#                                        card_num=card_num,
#                                        exp_date=exp_date,
#                                        card_cvv=cvv)
#     if response[0] == APPROVED:
#         transaction_id = response[6]
#
#         order = create_order(request, transaction_id)
#
#         results = {'order_number': order.id, 'message': ''}
#     if response[0] == DECLINED:
#         results = {'order_number': 0, 'message': 'There is a problemwith your credit card.'}
#     if response[0] == ERROR or response[0] == HELD_FOR_REVIEW:
#         results = {'order_number': 0, 'message': 'Error processing your order.'}
#     return results

@csrf_exempt
def create_order(request):
    val1 = json.loads(request.body)

    user_id = val1['user_id']

    cart = val1['cart']
    print(type(cart[0]))

    shipment = val1['payment']

    order = Order()
    order.user = user_id
    order.status = Order.SUBMITTED
    order.save()

    for item in cart:
        oi = OrderItem()
        oi.order = order
        oi.quantity = item['quantity']
        oi.price = item['price']
        oi.product = item['product']
        oi.save()

    val = create_payment(shipment, order.id)
    print(val['message'])
    if val['status_code'] == '200':

        resp = {'status': 'Success', 'status_code': '200', 'message': 'Order is completed.'}
    else:
        resp = {'status': 'Fail', 'status_code': '400', 'message': 'Order is fail.'}
        order.delete()

    return HttpResponse(json.dumps(resp), content_type='application/json')


def get_cartItems(cart_id):
    url = f'http://127.0.0.1:7000/product/{cart_id}'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    val = json.loads(response.content.decode('utf-8'))
    return val


def create_payment(payment, order_id):
    url = ' http://127.0.0.1:8000/initiate_payment/'
    headers = {'Content-Type': 'application/json'}
    print(payment["User Name"])
    data = {'User Name': payment["User Name"], "Order id": order_id, "Payment mode": payment["Payment mode"],
            "Mobile Number": payment["Mobile Number"]}
    print(data['User Name'])
    response = requests.post(url, data=data, headers=headers)
    val = json.loads(response.content.decode('utf-8'))
    return val
