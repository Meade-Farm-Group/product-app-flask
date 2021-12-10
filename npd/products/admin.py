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


class OperationsAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'created_on',
        'created_by',
    )


class FinishedProductAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'declared_weight_volume',
        'e_mark',
        'average_weight',
        'created_on',
        'created_by'
    )


class DefectSpecificationAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'defect',
        'amber',
        'red',
        'comment',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductStatus)
admin.site.register(Variety)
admin.site.register(Origin)
admin.site.register(CommercialModel, CommercialAdmin)
admin.site.register(PackagingModel, PackagingAdmin)
admin.site.register(OperationsModel, OperationsAdmin)
admin.site.register(FinishedProduct, FinishedProductAdmin)
admin.site.register(DefectSpecification, DefectSpecificationAdmin)
