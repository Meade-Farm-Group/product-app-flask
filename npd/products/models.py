from django.db import models
from django.contrib.auth.models import User
from ancillaries.models import Customer, Department, Supplier, Defect
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import date, timedelta
from products.sql_queries import get_varieties, get_origins, get_suppliers, get_packaging_suppliers


VARIETY_CHOICES = get_varieties()
ORIGIN_CHOICES = get_origins()
SUPPLIER_CHOICES = get_suppliers()
PACKAGING_SUPPLIER_CHOICES = get_packaging_suppliers()


class ProductStatus(models.Model):
    status = models.CharField(max_length=40)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = 'Product Statuses'


class Product(models.Model):
    product_name = models.CharField(max_length=40)
    department = models.ForeignKey(
        Department, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    start_date = models.DateField()
    status = models.ForeignKey(
        ProductStatus, null=True, on_delete=models.SET_NULL)
    signature = models.CharField(null=True, max_length=1000000)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def is_ready(self):
        return self.status == ProductStatus.objects.get(
            status="Completed - Production Ready")

    def is_final_confirmation(self):
        return self.status == ProductStatus.objects.get(
            status="Pending - Awaiting Final Confirmation")

    # methods to check how far out product is from starting
    def is_within_week(self):
        return date.today() + timedelta(days=7) >= self.start_date

    def is_within_fortnight(self):
        return date.today() + timedelta(days=14) >= self.start_date

    # For the product to be ready for signoff we require there to be at least
    # one instance of each of the following models
    def is_ready_for_signoff(self):
        if self.is_ready() or self.is_final_confirmation():
            return False

        checks = [
            CommercialModel,
            InnerPackaging,
            OuterPackaging,
            Palletisation,
            OperationsModel,
            DefectSpecification,
            FinishedProduct,
            ProphetModel
        ]

        for check in checks:
            if len(check.objects.filter(product=self)) == 0:
                return False

        return True

    def __str__(self):
        return str(self.product_name) + " - " + str(self.customer)


class CommercialModel(models.Model):

    class DeliveredState(models.TextChoices):
        CHILLED = 'CH', _('Chilled')
        AMBIENT = 'AM', _('Ambient')

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    product_branding = models.CharField(max_length=40)
    legal_product_description = models.CharField(max_length=40)
    case_count = models.IntegerField()
    weight_per_unit = models.CharField(max_length=20)
    product_code = models.IntegerField()
    delivered_state = models.CharField(
        max_length=2,
        choices=DeliveredState.choices,
        default=DeliveredState.CHILLED
    )
    product_inner_barcode = models.IntegerField()
    product_outer_barcode = models.IntegerField()
    size_diameter = models.CharField(max_length=40)
    storage_temperature = models.CharField(max_length=40)
    display_until = models.CharField(max_length=20)
    best_before = models.CharField(max_length=20)
    julian_code = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.product} Commercial Details'


class ApprovedOrigin(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    origin = models.CharField(choices=ORIGIN_CHOICES, max_length=100, null=True)

    def __str__(self):
        return f'{self.product} - {self.origin}'


class ApprovedVariety(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    variety = models.CharField(choices=VARIETY_CHOICES, max_length=100, null=True)

    def __str__(self):
        return f'{self.product} - {self.variety}'


class ApprovedSupplier(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    supplier = models.CharField(choices=SUPPLIER_CHOICES, max_length=100, null=True)

    def __str__(self):
        return f'{self.product} - {self.supplier}'


class OperationsModel(models.Model):

    class TestResult(models.TextChoices):
        OP = 'Operational', _('Operational')
        NOTOP = 'Not Operational', _('Not Operational')

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    test_date = models.DateField()
    packing_equipment_test = models.CharField(max_length=20)
    test_result = models.CharField(
        max_length=20,
        choices=TestResult.choices,
        default=TestResult.NOTOP
    )
    line_leader_trained = models.BooleanField()
    general_staff_trained = models.BooleanField()
    temp_storage_zone = models.CharField(max_length=20)
    storage_space_available = models.BooleanField()
    handling_equipment_available = models.BooleanField()
    packaging_on_site = models.BooleanField()
    raw_material_on_site = models.BooleanField()
    ready_for_product_run = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.product} Operations Details'


class FinishedProduct(models.Model):

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    declared_weight_volume = models.CharField(max_length=20)
    tare_weight = models.CharField(max_length=20)
    minimum_weight_volume = models.CharField(max_length=20)
    target_weight_volume = models.CharField(max_length=20)
    maximum_weight_volume = models.CharField(max_length=20)
    e_mark = models.BooleanField()
    average_weight = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.product} Finished Product Specification'


class DefectSpecification(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    defect = models.ForeignKey(Defect, on_delete=models.CASCADE)
    amber = models.DecimalField(max_digits=4, decimal_places=2)
    red = models.DecimalField(max_digits=4, decimal_places=2)
    comment = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.product} - {self.defect} Defect Specification'


class ProphetModel(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    product_created = models.BooleanField()
    bom_created = models.BooleanField()
    packaging_added = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.product} Prophet Model'


class InnerPackaging(models.Model):
    class PackagingTypes(models.TextChoices):
        CARDBOARD = 'Cardboard', _('Cardboard')
        PLASTIC = 'Plastic', _('Plastic')

    class Grades(models.TextChoices):
        ONE = '1', _('1')
        TWO = '2', _('2')
        NA = 'N/A', _('N/A')

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    branding = models.CharField(max_length=20)
    artwork_provided = models.BooleanField()
    supplier = models.CharField(
        choices=PACKAGING_SUPPLIER_CHOICES,
        max_length=100, null=True)
    packaging_type = models.CharField(
        max_length=20,
        choices=PackagingTypes.choices,
        default=PackagingTypes.CARDBOARD
    )
    packaging_grade = models.CharField(
        max_length=5,
        choices=Grades.choices,
        default=Grades.NA
    )
    dimensions = models.CharField(max_length=30)
    key_line = models.CharField(max_length=20)
    recyclable = models.BooleanField()
    biodegradable = models.BooleanField()
    packaging_ordered = models.BooleanField()
    date_ordered = models.DateField()
    delivery_date = models.DateField()
    packaging_in_stock = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.product} Inner Packaging Details'


class OuterPackaging(models.Model):
    class PackagingTypes(models.TextChoices):
        CARDBOARD = 'Cardboard', _('Cardboard')
        PLASTIC = 'Plastic', _('Plastic')

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    units_per_case = models.IntegerField()
    material_type = models.CharField(
        max_length=20,
        choices=PackagingTypes.choices,
        default=PackagingTypes.CARDBOARD
    )
    supplier = models.CharField(
        choices=PACKAGING_SUPPLIER_CHOICES,
        max_length=100, null=True)
    outer_dimensions = models.CharField(max_length=30)
    outer_case_label = models.BooleanField()
    outer_case_card = models.BooleanField()
    case_configuration = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.product} Outer Packaging Details'


class Palletisation(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    cases_per_pallet_layer = models.IntegerField()
    no_of_layers = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.product} Palletisation Details'
