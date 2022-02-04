from allauth.account.forms import SignupForm
from django import forms
from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from ancillaries.models import Department
from .models import Profile


class CustomSignupForm(SignupForm):

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=True
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        profile = Profile(
            user=user,
            department=self.cleaned_data['department']
        )
        viewer_group = Group.objects.get(name='Viewer')
        user.groups.add(viewer_group)
        profile.save()
        return user
