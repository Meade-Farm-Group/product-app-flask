from django.db import models
from django.contrib.auth.models import User
from ancillaries.models import Customer, Department, Supplier
from django.utils.translation import gettext_lazy as _


class ProductStatus(models.Model):
    status = models.CharField(max_length=40)

    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name_plural = 'Product Statuses'


class Product(models.Model):
    product_name = models.CharField(max_length=40)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(ProductStatus, null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.product_name) + " - " + str(self.customer)


class Variety(models.Model):
    variety_name = models.CharField(max_length=40)

    def __str__(self):
        return self.variety_name
    
    class Meta:
        verbose_name_plural = 'Varieties'


class Origin(models.Model):
    origin_name = models.CharField(max_length=40)

    def __str__(self):
        return self.origin_name


class CommercialModel(models.Model):

    class DeliveredState(models.TextChoices):
        CHILLED = 'CH', _('Chilled')
        AMBIENT = 'AM', _('Ambient')

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    start_date = models.DateField()
    product_branding = models.CharField(max_length=40)
    legal_product_description = models.CharField(max_length=40)
    case_count = models.IntegerField()
    weight_per_unit = models.CharField(max_length=20)
    product_code = models.IntegerField()
    delivered_state = models.CharField(
        max_length=2, 
        choices=DeliveredState.choices, 
        default=DeliveredState.CHILLED
    )
    product_inner_barcode = models.IntegerField()
    product_outer_barcode = models.IntegerField()
    size_diameter = models.CharField(max_length=40)
    storage_temperature = models.CharField(max_length=40)
    display_until = models.CharField(max_length=20)
    best_before = models.CharField(max_length=20)
    julian_code = models.CharField(max_length=10)
    approved_origins = models.ManyToManyField(Origin)
    approved_varieties = models.ManyToManyField(Variety)
    approved_suppliers = models.ManyToManyField(Supplier)

    def __str__(self):
        return f'{self.product} Commercial Details'
