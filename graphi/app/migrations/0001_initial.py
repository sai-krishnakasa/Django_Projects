# Generated by Django 4.1.1 on 2022-11-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Feature Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('in_stock', models.BooleanField(default=True, verbose_name='In Stock?')),
                ('date_created', models.DateTimeField(blank=True, null=True, verbose_name='Date created')),
                ('category', models.ManyToManyField(blank=True, to='app.category', verbose_name='Product categories')),
            ],
        ),
    ]
