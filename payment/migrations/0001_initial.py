# Generated by Django 3.2.6 on 2021-08-16 12:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gym', '0006_remove_userprofile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.CharField(default=0, max_length=200)),
                ('payment_date', models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 16, 12, 3, 23, 476669, tzinfo=utc))),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.member')),
            ],
        ),
    ]
