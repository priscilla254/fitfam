# Generated by Django 3.2.6 on 2021-08-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_auto_20210815_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
