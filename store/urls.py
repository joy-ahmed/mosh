
from django.urls import path
from .views import *

urlpatterns = [
    path('products/', product_view),
    path('product/<int:id>/', products_details),
    path('collections/<int:pk>/', collection_details, name='collection-detail'),
    path('collections/', collection_list, name='collection-list'),
]
