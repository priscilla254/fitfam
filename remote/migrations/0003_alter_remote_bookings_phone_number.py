# Generated by Django 3.2.6 on 2021-08-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote', '0002_alter_remote_bookings_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remote_bookings',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]