# Generated by Django 2.2.10 on 2021-03-29 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Department', models.CharField(max_length=50)),
                ('Contact', models.CharField(max_length=50)),
            ],
        ),
    ]
