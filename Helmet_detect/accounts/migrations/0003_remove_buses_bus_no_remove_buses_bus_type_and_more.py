# Generated by Django 4.1.1 on 2022-10-28 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_bus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buses',
            name='bus_no',
        ),
        migrations.RemoveField(
            model_name='buses',
            name='bus_type',
        ),
        migrations.RemoveField(
            model_name='buses',
            name='not_booked_seats',
        ),
        migrations.RemoveField(
            model_name='buses',
            name='seat_type',
        ),
        migrations.AddField(
            model_name='buses',
            name='bus',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.bus'),
        ),
    ]