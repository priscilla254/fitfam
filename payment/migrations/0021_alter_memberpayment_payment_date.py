# Generated by Django 3.2.6 on 2021-08-21 09:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0020_alter_memberpayment_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberpayment',
            name='payment_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 21, 9, 28, 33, 455898, tzinfo=utc)),
        ),
    ]
