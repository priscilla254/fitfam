# Generated by Django 3.2.6 on 2021-08-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='day',
            field=models.CharField(max_length=200, null=True),
        ),
    ]