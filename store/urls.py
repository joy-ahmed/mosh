
from django.urls import path
from .views import *

urlpatterns = [
    path('products/', product_view, name="products")
]