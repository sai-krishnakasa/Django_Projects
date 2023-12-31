# Generated by Django 4.1.1 on 2022-10-13 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_bookings_booking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='booking_Bus_details',
            field=models.ForeignKey(default='Anonymus', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='booking_bus', to='accounts.buses'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='booking_cust_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_cust', to=settings.AUTH_USER_MODEL),
        ),
    ]
