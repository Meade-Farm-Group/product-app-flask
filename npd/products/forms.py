from django import forms
from .models import DefectSpecification, FinishedProduct, OperationsModel, PackagingModel, Product, CommercialModel
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
