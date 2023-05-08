from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('clothes/',views.handle_request),
    path('clothes/',views.handle_request),
]
