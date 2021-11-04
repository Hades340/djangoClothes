from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
from django.db import models
from django import forms
#admin.site.site_header = "Clothes shop dashboard"
class categoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_type")
    list_filter = ("category_type",)
    search_fields = ['category_type']

class productAdmin(admin.ModelAdmin):
    list_display = ("id", "name","category" ,"img","decription","detail","price")
    list_filter = ("category_id",)
    search_fields = ['name']
    @admin.display(ordering='category_id')
    def category(self, obj):
        return obj.category_id.category_type

class product_detailAdmin(admin.ModelAdmin):
    list_display = ("name", "size", "color")
    list_filter = ("color","size")
    search_fields = ['name']

class customerAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "address","phone")
    list_filter = ("phone",)
    search_fields = ['username']

class orderAdmin(admin.ModelAdmin):
    list_display = ("id", "date_oder", "total")
    list_filter = ("date_oder",)
    search_fields = ['date_oder']

class order_detailAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product","quantity","total_price")
    list_filter = ("order_id",)
    search_fields = ['total_price']
    @admin.display(ordering='product')
    def product(self, obj):
        return obj.product_id.name
    
    @admin.display(ordering='order')
    def order(self, obj):
        return obj.order_id.date_oder
# Register your models here.
admin.site.register(category_product,categoryAdmin)
admin.site.register(product,productAdmin)
admin.site.register(product_detail,product_detailAdmin)
admin.site.register(customer,customerAdmin)
admin.site.register(order,orderAdmin)
admin.site.register(order_detail,order_detailAdmin)
