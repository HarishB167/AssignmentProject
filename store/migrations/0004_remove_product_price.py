# Generated by Django 3.2.13 on 2022-04-22 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_category_product_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
