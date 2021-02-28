from .urls import orders_list
from django.urls import path

urlpatterns = [
    path('', orders_list, name='orders-list'),
]
