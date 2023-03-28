from __future__ import unicode_literals

from datetime import date

from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from comment.models import Comment_Detail


def insert_comment(user_id,comment,product_id,is_active):
    comment_detail = Comment_Detail(user_id=user_id,comment=comment,is_active=is_active,product_id=product_id)
    comment_detail.save()
    return 1
@csrf_exempt
def add_comment(request):
    val = json.loads(request.body)
    resp = {}

    user_id = val.get('user_id')
    comment = val.get('comment')
    product_id = val.get('product_id')

    if user_id and comment and product_id:
        respdata = insert_comment(user_id=user_id,comment=comment,is_active=True,product_id= product_id)
        if respdata:
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

    return HttpResponse(json.dumps(resp,cls=DateEncoder), content_type='application/json')

@csrf_exempt
def get_comment_by_product(request,product_id):
    data = []
    resp = {}
    # This will fetch the data from the database.
    comment_details = Comment_Detail.objects.all()
    for tbl_value in comment_details.values():
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
    return HttpResponse(json.dumps(resp,cls=DateEncoder), content_type='application/json')


# @csrf_exempt
# def get_books(request):
#     data = []
#     resp = {}
#     # insert_book('11112', 'dark nhan tam', 'hoang', 'truyen', 'kim dong', '2020-12-21', 'avialable', '100', 'tryen hay',
#     #             20)
#     # This will fetch the data from the database.
#     prodata = Book.objects.all()
#     for tbl_value in prodata.values():
#         data.append(tbl_value)
#     # If data is available then it returns the data.
#     if data:
#         resp['status'] = 'Success'
#         resp['status_code'] = '200'
#         resp['data'] = data
#     else:
#         resp['status'] = 'Failed'
#         resp['status_code'] = '400'
#         resp['message'] = 'Data is not available.'
#     return HttpResponse(json.dumps(resp,cls=DateEncoder), content_type='application/json')
#
#
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d-%m-%Y')
        return super().default(obj)

