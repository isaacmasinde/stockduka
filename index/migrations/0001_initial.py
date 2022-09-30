# Generated by Django 2.2.10 on 2020-08-27 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Userdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contact', models.CharField(max_length=20)),
                ('Firstname', models.CharField(max_length=50)),
                ('Secondname', models.CharField(max_length=50)),
                ('Status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Sold', models.IntegerField()),
                ('Bought', models.IntegerField()),
                ('Brand', models.CharField(max_length=50)),
                ('Instock', models.BooleanField()),
                ('Measure', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Pic', models.ImageField(upload_to='pictures')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Biz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=50)),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Userdetail')),
            ],
        ),
    ]
