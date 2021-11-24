from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'department',
        'customer',
        'status',
        'created_on',
        'created_by',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductStatus)
