from django.contrib import admin
from . models import Products,OrderPdts,Order
# Register your models here.

admin.site.register(Products)
admin.site.register(OrderPdts)
admin.site.register(Order)