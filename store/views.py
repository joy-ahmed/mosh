from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


# Create your views here.

@api_view()
def product_view(request):
    querySet = Product.objects.all()
    serializer = ProductSerializer(querySet, many=True)
    return Response(serializer.data)


@api_view()
def products_details(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
