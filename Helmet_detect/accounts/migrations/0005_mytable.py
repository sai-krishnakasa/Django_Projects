# Generated by Django 4.1.1 on 2022-10-29 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_buses_bus_remove_buses_driver_details_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='myTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
            ],
        ),
    ]
