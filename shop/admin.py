from django.contrib import admin
from .models import Product, Cart, Cartitems

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cartitems)
