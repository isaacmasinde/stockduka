# Generated by Django 2.2.10 on 2020-08-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20200827_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='Pic',
        ),
        migrations.RemoveField(
            model_name='item',
            name='Quantity',
        ),
        migrations.AddField(
            model_name='brand',
            name='Pic',
            field=models.ImageField(null=True, upload_to='pictures'),
        ),
    ]
