# Generated by Django 4.1.1 on 2022-10-04 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_details',
            name='mobile',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
