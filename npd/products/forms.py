from django import forms
from .models import DefectSpecification, FinishedProduct, InnerPackaging, OperationsModel, OuterPackaging, Palletisation, Product, CommercialModel, ProphetModel
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


class FinishedProductForm(forms.ModelForm):
    """ Finished Product Form """
    class Meta:
        model = FinishedProduct
        exclude = [
            'product',
            'created_on',
            'created_by',
        ]


class DefectSpecificationForm(forms.ModelForm):
    """ Defect Specification Form """
    class Meta:
        model = DefectSpecification
        exclude = [
            'product',
        ]


class ProphetForm(forms.ModelForm):
    """ Prophet Form """
    class Meta:
        model = ProphetModel
        exclude = [
            'product',
            'created_on',
            'created_by',
        ]


class InnerPackagingForm(forms.ModelForm):
    """ Inner Packaging Form """
    class Meta:
        model = InnerPackaging
        exclude = [
            'product',
            'created_on',
            'created_by',
        ]
        widgets = {
            'date_ordered': DateInput(),
            'delivery_date': DateInput(),
        }


class OuterPackagingForm(forms.ModelForm):
    """ Outer Packaging Form """
    class Meta:
        model = OuterPackaging
        exclude = [
            'product',
            'created_on',
            'created_by',
        ]


class PalletisationForm(forms.ModelForm):
    """ Palletisation Form """
    class Meta:
        model = Palletisation
        exclude = [
            'product',
            'created_on',
            'created_by',
        ]
