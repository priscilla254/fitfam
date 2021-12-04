# Generated by Django 3.2.6 on 2021-08-26 10:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0035_alter_memberpayment_payment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberpayment',
            name='payment_amount',
        ),
        migrations.AddField(
            model_name='memberpayment',
            name='package',
            field=models.CharField(choices=[('weekly', 'weekly'), ('monthly', 'monthly'), ('yearly', 'yearly')], default=12, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='memberpayment',
            name='payment_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 26, 10, 46, 46, 180190, tzinfo=utc)),
        ),
    ]
