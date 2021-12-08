from django import forms
from .models import OperationsModel, PackagingModel, Product, CommercialModel
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


class PackagingForm(forms.ModelForm):
    """ Packaging Form """
    class Meta:
        model = PackagingModel
        exclude = [
            'product',
            'created_on',
            'created_by',
        ]
        widgets = {
            'date_ordered': DateInput(),
            'delivery_date': DateInput(),
        }


class OperationsForm(forms.ModelForm):
    """ Operations Form """
    class Meta:
        model = OperationsModel
        exclude = [
            'product',
            'created_on',
            'created_by',
        ]
        widgets = {
            'test_date': DateInput(),
        }
