# Generated by Django 2.2.10 on 2020-08-30 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_cart_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='Cut',
            new_name='Discount',
        ),
    ]