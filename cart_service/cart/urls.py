from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('cart/<str:cart_id>/',views.handle_request),


    # path('shipment_updates/', views.shipment_reg_update)
]
