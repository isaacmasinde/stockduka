# Generated by Django 2.2.10 on 2020-09-01 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0017_auto_20200831_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.Category'),
        ),
    ]