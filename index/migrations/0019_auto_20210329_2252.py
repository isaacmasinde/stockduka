# Generated by Django 2.2.10 on 2021-03-29 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0018_item_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biz',
            options={'ordering': ['Name']},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['Name']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['Name']},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['Name']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['User']},
        ),
        migrations.AlterField(
            model_name='brand',
            name='Bought',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='brand',
            name='Sold',
            field=models.IntegerField(),
        ),
    ]
