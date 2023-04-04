from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.get_product_data),
    path('product/<str:product_id>/',views.get_product),
    path('product/',views.add_product),

    # path('product/<str:product_id>/',views.update_product_quantity),

]
