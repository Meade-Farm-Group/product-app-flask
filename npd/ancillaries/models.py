from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Department(models.Model):
    department_name = models.CharField(max_length=20)

    def __str__(self):
        return self.department_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=40)
    supplier_code = models.IntegerField(default=1, validators=[
        MaxValueValidator(99999999),
        MinValueValidator(1)
    ])

    def __str__(self):
        return self.supplier_name
