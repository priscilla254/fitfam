# Generated by Django 3.2.6 on 2021-08-25 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='phone_number',
            field=models.FloatField(default=23),
            preserve_default=False,
        ),
    ]
