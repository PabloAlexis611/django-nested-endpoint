# Generated by Django 3.2.9 on 2021-11-07 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_manufacturer_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine_type',
            field=models.CharField(choices=[('Electric', 'Electric'), ('V6', 'V6'), ('V8', 'V8'), ('V12', 'V12')], max_length=8, verbose_name='Engine Type'),
        ),
    ]
