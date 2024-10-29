from django.contrib import admin
from .models import Supplier, Product, StockTransaction,Profile,Cashier,Notification

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(StockTransaction)
admin.site.register(Profile)
admin.site.register(Notification)
admin.site.register(Cashier)