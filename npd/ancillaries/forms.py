from django import forms

from .models import Customer, Defect


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class DefectForm(forms.ModelForm):
    class Meta:
        model = Defect
        fields = [
            'defect_name',
        ]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'customer_name',
        ]
