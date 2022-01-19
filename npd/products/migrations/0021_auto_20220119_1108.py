# Generated by Django 3.2.9 on 2022-01-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20220118_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='commercialmodel',
            name='packed_here',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('B', 'Both')], default='Y', max_length=1),
        ),
        migrations.AlterField(
            model_name='finishedproduct',
            name='tare_weight',
            field=models.CharField(max_length=20),
        ),
    ]