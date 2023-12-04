from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


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
        serializer.save()
        print(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def products_details(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if product.orderitem_set.count() > 0:
            return Response({'error': 'Product can not be deleted cause it associated with orderitem'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.annotate(products_count=Count('product')).all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def collection_details(request, pk):
    collection = get_object_or_404(
        Collection.objects.annotate(products_count=Count('product')), pk=pk
    )
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if collection.product.count() > 0:
            return Response({'error': 'Collection can not be deleted'})
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)