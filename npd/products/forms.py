from django import forms

from .models import (
    ApprovedOrigin,
    ApprovedSupplier,
    ApprovedVariety,
    DefectSpecification,
    FinishedProduct,
    InnerPackaging,
    OperationsModel,
    OuterPackaging,
    Palletisation,
    Product,
    CommercialModel,
    ProphetModel
)
from ancillaries.forms import DateInput


class ProductForm(forms.ModelForm):
    """ Product Form """
    class Meta:
        model = Product
        exclude = [
            'signature',
            'status',
            'created_on',
            'created_by',
        ]
        widgets = {
            'start_date': DateInput(),
        }


class CommercialForm(forms.ModelForm):
    """ Commercial Form """
    class Meta:
        model = CommercialModel
        exclude = [
            'product',
            'created_on',
            'created_by',
        ]
        labels = {
            "product_code": "Supplier Product Code",
            "display_until": "Display Until (days)",
            "best_before": "Best Before (days)",
        }
        widgets = {
            'packed_here': forms.RadioSelect(),
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


class SignOffForm(forms.Form):
    signature_data = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'd-none',
            'id': 'signature-data',
        }
    ), label='')


class ApprovedVarietyForm(forms.ModelForm):
    """ Approved Variety Form """
    class Meta:
        model = ApprovedVariety
        fields = [
            'variety',
        ]


class ApprovedOriginForm(forms.ModelForm):
    """ Approved Origin Form """
    class Meta:
        model = ApprovedOrigin
        fields = [
            'origin',
        ]


class ApprovedSupplierForm(forms.ModelForm):
    """ Approved Supplier Form """
    class Meta:
        model = ApprovedSupplier
        fields = [
            'supplier'
        ]
