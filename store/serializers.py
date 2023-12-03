from decimal import Decimal
from rest_framework import serializers
from store.models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(method_name='get_tax_methods')

    
    #tax maethods
    def get_tax_methods(self, product: Product): #type anotation
        price = product.price * Decimal(1.1)
        return round(price, 2)