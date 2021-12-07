from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import CommercialModel, Product, ProductStatus
from .forms import CommercialForm, ProductForm
from django.contrib import messages


@login_required
def all_products(request):
    products = Product.objects.all()

    return render(request, 'products/product_table.html', {
        'products': products
    })


@login_required
def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    exclude_fields = ["id", "product"]
    commercial_details = CommercialModel.objects.filter(product=product_id).first()

    return render(request, 'products/product_details.html', {
        'product': product,
        'commercial_details': commercial_details,
        'commercial_details_keys': CommercialModel._meta.get_fields(),
        'exclude_fields': exclude_fields
    })


@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.status = ProductStatus.objects.get(status='Pending - Awaiting Sign Off')
            product.created_by = request.user
            product.save()
            messages.success(request, "Product Created Successfully!")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Creating Product! Please Try Again")
    else:
        form = ProductForm()

    return render(request, 'products/product_form.html', {
        'form': form
    })


    })
