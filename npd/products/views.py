from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import CommercialModel, DefectSpecification, FinishedProduct, InnerPackaging, OperationsModel, OuterPackaging, Palletisation, Product, ProductStatus, ProphetModel
from .forms import CommercialForm, DefectSpecificationForm, FinishedProductForm, InnerPackagingForm, OperationsForm, OuterPackagingForm, PalletisationForm, ProductForm, ProphetForm
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

    # fields we don't want displayed in the template
    exclude_fields = ["id", "product"]
    # we want the commercial_details variable to return none if they haven't been added
    commercial_details = CommercialModel.objects.filter(product=product_id).first()
    operations_details = OperationsModel.objects.filter(product=product_id).first()
    inner_packaging = InnerPackaging.objects.filter(product=product_id)
    outer_packaging = OuterPackaging.objects.filter(product=product_id)
    palletisation = Palletisation.objects.filter(product=product_id).first()
    finished_product = FinishedProduct.objects.filter(product=product_id).first()
    defect_specs = DefectSpecification.objects.filter(product=product_id)
    prophet_details = ProphetModel.objects.filter(product=product_id).first()

    return render(request, 'products/product_details.html', {
        'product': product,
        'commercial_details': commercial_details,
        'commercial_details_keys': CommercialModel._meta.get_fields(),
        'operations_details': operations_details,
        'operations_details_keys': OperationsModel._meta.get_fields(),
        'inner_packaging': inner_packaging,
        'inner_packaging_keys': InnerPackaging._meta.get_fields(),
        'outer_packaging': outer_packaging,
        'outer_packaging_keys': OuterPackaging._meta.get_fields(),
        'palletisation': palletisation,
        'palletisation_keys': Palletisation._meta.get_fields(),
        'finished_product': finished_product,
        'finished_product_keys': FinishedProduct._meta.get_fields(),
        'defect_specs': defect_specs,
        'defect_spec_keys': DefectSpecification._meta.get_fields(),
        'prophet_details': prophet_details,
        'prophet_details_keys': ProphetModel._meta.get_fields(),
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


@login_required
def edit_navigation(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    commercial_details = CommercialModel.objects.filter(product=product_id).first()
    operations_details = OperationsModel.objects.filter(product=product_id).first()
    prophet_details = ProphetModel.objects.filter(product=product_id).first()

    return render(request, 'products/edit_navigation.html', {
        'product': product,
        'commercial_details': commercial_details,
        'operations_details': operations_details,
        'prophet_details': prophet_details,
    })


@login_required
def add_commercial_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if len(CommercialModel.objects.filter(product=product_id)) > 0:
        messages.error(request, f"Commercial Details Already Submitted For {product.product_name}")
        return redirect(reverse(product_details, args=[product.id]))
    if request.method == 'POST':
        form = CommercialForm(request.POST)
        if form.is_valid():
            commercial_details = form.save(commit=False)
            commercial_details.product = product
            commercial_details.created_by = request.user
            commercial_details.save()
            form.save_m2m()
            messages.success(request, "Commercial Details Successfully Added!")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Adding Commercial Details! Please Try Again")
    else:
        form = CommercialForm()
    
    return render(request, 'products/commercial_form.html', {
        'context': 'add',
        'product': product,
        'form': form
    })


@login_required
def edit_commercial_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    commercial_details = get_object_or_404(CommercialModel, product=product_id)

    if request.method == 'POST':
        form = CommercialForm(request.POST, instance=commercial_details)
        if form.is_valid():
            commercial_details = form.save()
            messages.success(request, "Commercial Details Successfully Updated!")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Updating Commercial Details! Please Try Again")
    else:
        form = CommercialForm(instance=commercial_details)

    return render(request, 'products/commercial_form.html', {
        'context': 'edit',
        'product': product,
        'form': form
    })


@login_required
def add_operations_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if len(OperationsModel.objects.filter(product=product_id)) > 0:
        messages.error(request, f"Operations Details Already Submitted For {product.product_name}")
        return redirect(reverse(product_details, args=[product.id]))
    if request.method == 'POST':
        form = OperationsForm(request.POST)
        if form.is_valid():
            operations_details = form.save(commit=False)
            operations_details.product = product
            operations_details.created_by = request.user
            operations_details.save()
            form.save_m2m()
            messages.success(request, "Operational Details Successfully Added!")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Adding Operational Details! Please Try Again")
    else:
        form = OperationsForm()

    return render(request, 'products/operations_form.html', {
        'context': 'add',
        'product': product,
        'form': form
    })


@login_required
def edit_operations_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    operations_details = get_object_or_404(OperationsModel, product=product_id)

    if request.method == 'POST':
        form = OperationsForm(request.POST, instance=operations_details)
        if form.is_valid():
            operations_details = form.save()
            messages.success(request, "Opeartions Details Successfully Updated!")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Updating Operational Details! Please Try Again")
    else:
        form = OperationsForm(instance=operations_details)

    return render(request, 'products/operations_form.html', {
        'context': 'edit',
        'product': product,
        'form': form
    })


@login_required
def technical_navigation(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    finished_spec = FinishedProduct.objects.filter(product=product_id).first()

    return render(request, 'products/technical_navigation.html', {
        'product': product,
        'finished_spec': finished_spec,
    })


@login_required
def add_finished_specification(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if len(FinishedProduct.objects.filter(product=product_id)) > 0:
        messages.error(request, f"Finished Product Specification Already Submitted For {product.product_name}")
        return redirect(reverse(product_details, args=[product.id]))

    if request.method == 'POST':
        form = FinishedProductForm(request.POST)
        if form.is_valid():
            commercial_details = form.save(commit=False)
            commercial_details.product = product
            commercial_details.created_by = request.user
            commercial_details.save()
            messages.success(request, "Finished Product Specification Successfully Added!")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Adding Finished Product Specification! Please Try Again")
    else:
        form = FinishedProductForm()

    return render(request, 'products/finished_product_form.html', {
        'context': 'add',
        'product': product,
        'form': form,
    })


@login_required
def edit_finished_specification(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    finished_spec = get_object_or_404(FinishedProduct, product=product_id)

    if request.method == 'POST':
        form = FinishedProductForm(request.POST, instance=finished_spec)
        if form.is_valid():
            finished_spec = form.save()
            messages.success(request, "Finished Product Specification Successfully Updated!")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Updating Finished Product Specification! Please Try Again")
    else:
        form = FinishedProductForm(instance=finished_spec)
    
    return render(request, 'products/finished_product_form.html', {
        'context': 'edit',
        'product': product,
        'form': form,
    })


@login_required
def add_defect_specification(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = DefectSpecificationForm(request.POST)
        if form.is_valid():
            defect_spec = form.save(commit=False)
            defect_spec.product = product
            defect_spec.save()
            messages.success(request, "Defect Specification Successfully Added!")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Adding Defect Specification! Please Try Again")
    else:
        form = DefectSpecificationForm()

    return render(request, 'products/defect_specification_form.html', {
        'context': 'add',
        'product': product,
        'form': form,
    })


@login_required
def edit_defect_specification(request, product_id, defect_spec_id):
    product = get_object_or_404(Product, pk=product_id)
    defect_spec = get_object_or_404(DefectSpecification, pk=defect_spec_id)

    if defect_spec.product != product:
        messages.warning("Invalid Product/Spec! Please Try Again")
        return redirect(reverse(all_products))
    
    if request.method == 'POST':
        form = DefectSpecificationForm(request.POST, instance=defect_spec)
        if form.is_valid():
            defect_spec = form.save()
            messages.success(request, "Defect Specification Successfully Updated!")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Updating Defect Specification! Please Try Again")
    else:
        form = DefectSpecificationForm(instance=defect_spec)
    
    return render(request, 'products/defect_specification_form.html', {
        'context': 'edit',
        'product': product,
        'defect_spec': defect_spec,
        'form': form
    })


@login_required
def product_defects(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    defects = DefectSpecification.objects.filter(product=product)

    return render(request, 'products/defect_table.html', {
        'product': product,
        'defects': defects,
    })


@login_required
def delete_defect_specification(request, product_id, defect_spec_id):
    product = get_object_or_404(Product, pk=product_id)
    defect_spec = get_object_or_404(DefectSpecification, pk=defect_spec_id)

    if request.method == 'POST':
        defect_spec.delete()
        messages.warning(request, "Defect Specification Successfully Deleted!")
        return redirect(reverse(product_details, args=[product.id]))

    return render(request, 'products/confirm_delete.html', {
        'delete': 'Defect Specification',
        'action': reverse(delete_defect_specification, args=[product.id, defect_spec.id]),
        'cancel': reverse(product_details, args=[product.id]),
    })


@login_required
def add_prophet_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if len(ProphetModel.objects.filter(product=product_id)) > 0:
        messages.error(request, f"Prophet Details Already Submitted For {product.product_name}")
        return redirect(reverse(product_details, args=[product.id]))
    if request.method == 'POST':
        form = ProphetForm(request.POST)
        if form.is_valid():
            prophet_details = form.save(commit=False)
            prophet_details.product = product
            prophet_details.created_by = request.user
            prophet_details.save()
            messages.success(request, "Prophet Details Successfully Added!")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Adding Prophet Details! Please Try Again")
    else:
        form = ProphetForm()
    
    return render(request, 'products/prophet_form.html', {
        'context': 'add',
        'product': product,
        'form': form
    })


@login_required
def edit_prophet_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    prophet_details = get_object_or_404(ProphetModel, product=product_id)

    if request.method == 'POST':
        form = ProphetForm(request.POST, instance=prophet_details)
        if form.is_valid():
            prophet_details = form.save()
            messages.success(request, "Prophet Details Successfully Updated!")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Updating Prophet Details! Please Try Again")
    else:
        form = ProphetForm(instance=prophet_details)

    return render(request, 'products/prophet_form.html', {
        'context': 'edit',
        'product': product,
        'form': form
    })


@login_required
def packaging_navigation(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    palletisation = Palletisation.objects.filter(product=product_id).first()

    return render(request, 'products/packaging_navigation.html', {
        'product': product,
        'palletisation': palletisation,
    })


@login_required
def add_palletisation_spec(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if len(Palletisation.objects.filter(product=product_id)) > 0:
        messages.error(request, f"Palletisation Details Already Submitted For {product.product_name}")
        return redirect(reverse(product_details, args=[product.id]))
    if request.method == 'POST':
        form = PalletisationForm(request.POST)
        if form.is_valid():
            palletisation_details = form.save(commit=False)
            palletisation_details.product = product
            palletisation_details.created_by = request.user
            palletisation_details.save()
            messages.success(request, "Palletisation Details Successfully Added!")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Adding Palletisation Details! Please Try Again")
    else:
        form = PalletisationForm()
    
    return render(request, 'products/palletisation_form.html', {
        'context': 'add',
        'product': product,
        'form': form
    })


@login_required
def edit_palletisation_spec(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    palletisation_details = get_object_or_404(Palletisation, product=product_id)

    if request.method == 'POST':
        form = PalletisationForm(request.POST, instance=palletisation_details)
        if form.is_valid():
            palletisation_details = form.save()
            messages.success(request, "Palletisation Details Successfully Updated")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Updating Palletisation Details! Please Try Again")
    else:
        form = PalletisationForm(instance=palletisation_details)

    return render(request, 'products/palletisation_form.html', {
        'context': 'edit',
        'product': product,
        'form': form
    })


@login_required
def inner_packaging_table(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    inner_packaging = InnerPackaging.objects.filter(product=product)

    return render(request, 'products/inner_packaging_table.html', {
        'product': product,
        'inner_packaging': inner_packaging,
    })


@login_required
def add_inner_packaging(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = InnerPackagingForm(request.POST)
        if form.is_valid():
            inner_packaging = form.save(commit=False)
            inner_packaging.product = product
            inner_packaging.created_by = request.user
            inner_packaging.save()
            messages.success(request, "Inner Packaging Details Successfully Added!")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Adding Inner Packaging Details! Please Try Again")
    else:
        form = InnerPackagingForm()
    
    return render(request, 'products/inner_packaging_form.html', {
        'context': 'add',
        'product': product,
        'form': form
    })


@login_required
def edit_inner_packaging(request, product_id, inner_pack_id):
    product = get_object_or_404(Product, pk=product_id)
    inner_packaging = get_object_or_404(InnerPackaging, pk=inner_pack_id)

    if request.method == 'POST':
        form = InnerPackagingForm(request.POST, instance=inner_packaging)
        if form.is_valid():
            inner_packaging = form.save()
            messages.success(request, "Inner Packaging Details Successfully Updated")
            return redirect(reverse(product_details, args=[product.id]))
        else:
            messages.error(request, "Error Updating Inner Packaging Details! Please Try Again")
    else:
        form = InnerPackagingForm(instance=inner_packaging)

    return render(request, 'products/inner_packaging_form.html', {
        'context': 'edit',
        'product': product,
        'inner_packaging': inner_packaging,
        'form': form
    })


@login_required
def outer_packaging_table(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    outer_packaging = OuterPackaging.objects.filter(product=product)

    return render(request, 'products/outer_packaging_table.html', {
        'product': product,
        'outer_packaging': outer_packaging,
    })


