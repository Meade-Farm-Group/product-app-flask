from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Defect)