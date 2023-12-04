from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def product_view(request):
    if request.method == 'GET':
        querySet = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(querySet, many=True, context={'request': request}) #context for hyperlinkerelated fields
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.validated_data
        #     return Response('ok')
        # else:
        #     return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        return Response('ok')

@api_view()
def products_details(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view()
def collection_details(request, id):
    return Response('ok')