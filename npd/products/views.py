from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CommercialModel, Product
from django.core.serializers import serialize


@login_required
def all_products(request):
    products = Product.objects.all()

    return render(request, 'products/product_table.html', {
        'products': products
    })


@login_required
def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    commercial_details = serialize("python", CommercialModel.objects.filter(product=product))

    return render(request, 'products/product_details.html', {
        'product': product,
        'commercial_details': commercial_details,
        'commercial_details_keys': CommercialModel._meta.get_fields(),
    })
