# Generated by Django 3.0.5 on 2020-08-03 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200803_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_quantity',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='thumbnail_file',
            new_name='thumbnail',
        ),
    ]
