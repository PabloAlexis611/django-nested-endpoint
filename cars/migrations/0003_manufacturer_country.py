# Generated by Django 3.2.9 on 2021-11-06 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_year_car_prod_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='country',
            field=models.CharField(default='USA', max_length=50, verbose_name='Country'),
            preserve_default=False,
        ),
    ]
