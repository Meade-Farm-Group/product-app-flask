from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from products.models import Product, ProductStatus

@login_required
def user_tasks(request):
    group = request.user.groups.first()
    outstanding_products = Product.objects.filter(
        ~Q(status=ProductStatus.objects.get(status="Completed - Production Ready"))
    )
    user_products = []
    for product in outstanding_products:
        if group.name in product.outstanding_checks():
            user_products.append(product)

    return render(request, 'users/user_tasks.html', {
        'user_products': user_products,
    })
