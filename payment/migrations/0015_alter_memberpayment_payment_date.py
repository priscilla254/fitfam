# Generated by Django 3.2.6 on 2021-08-18 12:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0014_alter_memberpayment_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberpayment',
            name='payment_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 18, 12, 8, 5, 508839, tzinfo=utc)),
        ),
    ]
