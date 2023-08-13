# Generated by Django 4.1.1 on 2022-10-26 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_bookings_booking_bus_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='booking_Bus_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='booking_bus', to='accounts.buses'),
        ),
        migrations.AlterField(
            model_name='buses',
            name='destination',
            field=models.CharField(choices=[('Ongole', 'Ongole'), ('Bhadrachalam', 'Bhadrachalam'), ('chittor', 'Chittor'), ('ahmedabad', 'Ahmedabad'), ('vizag', 'vizag'), ('delhi', 'delhi'), ('pune', 'Pune'), ('chittor', 'Chittor'), ('Banglore', 'Banglore'), ('rajastan', 'rajastan'), ('chennai', 'chennai'), ('Hyderabad', 'Hyderabad'), ('Nellore', 'Nellore'), ('bhopal', 'Bhopal'), ('vijayawada', 'vijayawada'), ('srinagar', 'Srinagar'), ('kanpur', 'Kanpur'), ('patna', 'Patna'), ('indore', 'Indore')], max_length=30),
        ),
    ]
