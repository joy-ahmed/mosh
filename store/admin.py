from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'price']

admin.site.register(Collection)
admin.site.register(Promotion)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(CartItem)
