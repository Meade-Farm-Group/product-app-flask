from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'department',
        'customer',
        'start_date',
        'status',
        'created_on',
        'created_by',
    )


class CommercialAdmin(admin.ModelAdmin):
    list_display = (
        'product',
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


class ProphetModelAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'product_created',
        'bom_created',
        'packaging_added',
        'created_on',
        'created_by',
    )


class InnerPackagingAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'branding',
        'packaging_type',
        'created_on',
        'created_by',
    )


class OuterPackagingAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'material_type',
        'supplier',
        'outer_dimensions',
        'created_on',
        'created_by',
    )


class PalletisationAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'cases_per_pallet_layer',
        'no_of_layers',
        'created_on',
        'created_by',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductStatus)
admin.site.register(Variety)
admin.site.register(Origin)
admin.site.register(CommercialModel, CommercialAdmin)
admin.site.register(OperationsModel, OperationsAdmin)
admin.site.register(FinishedProduct, FinishedProductAdmin)
admin.site.register(DefectSpecification, DefectSpecificationAdmin)
admin.site.register(ProphetModel, ProphetModelAdmin)
admin.site.register(InnerPackaging, InnerPackagingAdmin)
admin.site.register(OuterPackaging, OuterPackagingAdmin)
admin.site.register(Palletisation, PalletisationAdmin)
