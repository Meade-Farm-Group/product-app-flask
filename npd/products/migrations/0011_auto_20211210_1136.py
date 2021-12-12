# Generated by Django 3.2.9 on 2021-12-10 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ancillaries', '0003_defect'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0010_prophetmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='InnerPackaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branding', models.CharField(max_length=20)),
                ('artwork_provided', models.BooleanField()),
                ('packaging_type', models.CharField(choices=[('Cardboard', 'Cardboard'), ('Plastic', 'Plastic')], default='Cardboard', max_length=20)),
                ('packaging_grade', models.CharField(choices=[('1', '1'), ('2', '2'), ('N/A', 'N/A')], default='N/A', max_length=5)),
                ('dimensions', models.CharField(max_length=30)),
                ('key_line', models.CharField(max_length=20)),
                ('recyclable', models.BooleanField()),
                ('biodegradable', models.BooleanField()),
                ('packaging_ordered', models.BooleanField()),
                ('date_ordered', models.DateField()),
                ('delivery_date', models.DateField()),
                ('packaging_in_stock', models.BooleanField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ancillaries.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='OuterPackaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units_per_case', models.IntegerField()),
                ('material_type', models.CharField(choices=[('Cardboard', 'Cardboard'), ('Plastic', 'Plastic')], default='Cardboard', max_length=20)),
                ('outer_dimensions', models.CharField(max_length=30)),
                ('outer_case_label', models.BooleanField()),
                ('outer_case_card', models.BooleanField()),
                ('case_configuration', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ancillaries.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Palletisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cases_per_pallet_layer', models.IntegerField()),
                ('no_of_layers', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.DeleteModel(
            name='PackagingModel',
        ),
    ]