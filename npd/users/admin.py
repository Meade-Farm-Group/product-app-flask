from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'department',
    )


admin.site.register(Profile, ProfileAdmin)
