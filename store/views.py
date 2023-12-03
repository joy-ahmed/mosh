from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
# Create your views here.

@api_view()
def product_view(request):
    return Response('ok')


