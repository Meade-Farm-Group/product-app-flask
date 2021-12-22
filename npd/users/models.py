from django.db import models
from django.contrib.auth.models import User
from ancillaries.models import Department
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.user} Profile'
