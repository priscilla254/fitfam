# Generated by Django 3.2.6 on 2021-08-25 10:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0028_alter_memberpayment_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberpayment',
            name='payment_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 25, 10, 11, 52, 852076, tzinfo=utc)),
        ),
    ]
