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


class CommercialAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'start_date',
        'legal_product_description',
        'case_count',
        'weight_per_unit',
        'product_code',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductStatus)
admin.site.register(Variety)
admin.site.register(Origin)
admin.site.register(CommercialModel, CommercialAdmin)
