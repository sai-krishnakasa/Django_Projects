# Generated by Django 4.1.1 on 2022-09-23 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_author_dod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='dod',
            field=models.DateField(blank=True, default=''),
        ),
    ]
