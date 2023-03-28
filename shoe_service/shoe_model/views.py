from __future__ import unicode_literals

from datetime import date

from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from shoe_model.models import Shoe


def insert_shoe(shoe_id,title,category,brand,availability,price,description,quantity,size):
    book_data = Shoe(shoe_id=shoe_id,name=title,category=category,brand=brand,quantity=quantity,availability=availability,description=description,price=price,size=size)
    book_data.save()
    return 1


@csrf_exempt
def get_shoes(request):
    data = []
    resp = {}
    # insert_shoe('11112', 'giay', 'giay nam', 'vn',  'avialable', 100, 'giay hay',20,34)
    # This will fetch the data from the database.
    prodata = Shoe.objects.all()
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
    return HttpResponse(json.dumps(resp,cls=DateEncoder), content_type='application/json')


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d-%m-%Y')
        return super().default(obj)

