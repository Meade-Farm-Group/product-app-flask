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


