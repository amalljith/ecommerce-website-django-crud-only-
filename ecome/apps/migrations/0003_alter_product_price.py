# Generated by Django 4.2.4 on 2023-09-28 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
