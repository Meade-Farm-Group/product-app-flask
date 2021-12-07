from django import forms
from .models import Product, CommercialModel
from ancillaries.forms import DateInput


class ProductForm(forms.ModelForm):
    """ Product Form """
    class Meta:
        model = Product
        exclude = [
            'status',
            'created_on',
            'created_by',
        ]


class CommercialForm(forms.ModelForm):
    """ Commercial Form """
    class Meta:
        model = CommercialModel
        exclude = [
            'product',
            'created_on',
            'created_by',
        ]
        widgets = {
            'start_date': DateInput(),
        }
