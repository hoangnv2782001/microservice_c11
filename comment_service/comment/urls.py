from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('cart/<int:product_id>', views.add_to_cart),
    path('comment/',views.add_comment),
    path('comment/<str:product_id>',views.get_comment_by_product),

    # path('shipment_updates/', views.shipment_reg_update)
]
