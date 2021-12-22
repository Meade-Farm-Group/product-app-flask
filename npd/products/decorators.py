from django.shortcuts import get_object_or_404, redirect, reverse
from django.utils.functional import wraps
from django.contrib import messages
from .models import Product


# decorator that checks product status and redirects if production ready
def check_product_status(view):
    @wraps(view)
    def inner(request, product_id, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_id)

        if product.is_ready():
            messages.warning(
                request, "Production Ready Products Cannot Be Edited!")
            return redirect(reverse('product_details', args=[product.id]))

        return view(request, product_id, *args, **kwargs)

    return inner
