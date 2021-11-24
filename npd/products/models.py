from django.db import models
from django.contrib.auth.models import User
from ancillaries.models import Customer, Department


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
