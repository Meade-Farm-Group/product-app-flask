from django.template.defaulttags import register
from products.models import *


@register.filter
def lookup(object, key):
    if hasattr(object, key):
        return getattr(object, key)
    
    return None


@register.filter
def get_type(value):
    if value.__class__.__name__ == "ManyRelatedManager":
        return "list"
    else:
        return "str"


@register.filter
def is_viewer(user):
    return user.groups.filter(name="Viewer").exists()


@register.filter
def outstanding_tasks(user, product):
    checks = {
        "Commercial": [
            CommercialModel,
            ApprovedOrigin,
            ApprovedSupplier,
        ],
        "Packaging": [
            InnerPackaging,
            OuterPackaging,
            Palletisation,
        ],
        "Operations": [
            OperationsModel
        ],
        "Technical": [
            DefectSpecification,
            FinishedProduct,
        ],
        "Prophet": [
            ProphetModel,
        ]
    }
    outstanding_tasks = product.outstanding_checks()
    user_group = user.groups.all().first().name
    
    user_outstanding = []

    if user_group in outstanding_tasks:
        for model in checks[user_group]:
            done = False
            if len(model.objects.filter(product=product)) > 0:
                done = True
            user_outstanding.append({
                "name": model._meta.verbose_name.title(), 
                "done": done,
            })

    return user_outstanding
