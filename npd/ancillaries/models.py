from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=20)

    def __str__(self):
        return self.department_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name
