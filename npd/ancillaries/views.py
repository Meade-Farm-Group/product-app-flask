from django.shortcuts import get_object_or_404, render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Customer, Defect
from .forms import DefectForm, CustomerForm


@login_required
@permission_required('products.add_finishedproduct', raise_exception=True)
def view_defects(request):
    defects = Defect.objects.all()
    
    return render(request, 'ancillaries/defect_table.html', {
        'defects': defects,
    })


@login_required
@permission_required('products.add_finishedproduct', raise_exception=True)
def add_defect(request):
    if request.method == 'POST':
        form = DefectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Defect Created Successfully!")
            return redirect(reverse(view_defects))
        else:
            messages.error(request, "Error Creating Defect! Please Try Again!")
    else:
        form = DefectForm()

    return render(request, 'ancillaries/defect_form.html', {
        'form': form
    })


@login_required
@permission_required('product.add_finishedproduct', raise_exception=True)
def delete_defect(request, defect_id):
    defect = get_object_or_404(Defect, pk=defect_id)

    if request.method == 'POST':
        defect.delete()
        messages.warning(request, "Defect Successfully Deleted!")
        return redirect(reverse(view_defects))
    
    return render(request, 'products/confirm_delete.html', {
        'delete': 'Defect',
        'action': reverse(
            delete_defect, args=[defect.id]
        ),
        'cancel': reverse(view_defects)
    })


@login_required
@permission_required('product.add_finishedproduct', raise_exception=True)
def view_customers(request):
    customers = Customer.objects.all()

    return render(request, 'ancillaries/customer_table.html', {
        'customers': customers,
    })


@login_required
@permission_required('product.add_finishedproduct', raise_exception=True)
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Customer Successfully Added!"
            )
            return redirect(reverse(view_customers))
        else:
            messages.error(
                request, 'Error Adding Customer! Please Try Again'
            )
    else:
        form = CustomerForm()

    return render(request, 'ancillaries/customer_form.html', {
        'form': form,
    })
