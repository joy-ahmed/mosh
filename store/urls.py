
from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('product/<int:id>/', ProductDetail.as_view()),
    path('collections/<int:pk>/', collection_details, name='collection-detail'),
    path('collections/', collection_list, name='collection-list'),
]
