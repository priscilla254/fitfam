# Generated by Django 3.2.6 on 2021-08-17 16:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_memberpayment_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberpayment',
            name='payment_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 17, 16, 31, 32, 640160, tzinfo=utc)),
        ),
    ]
