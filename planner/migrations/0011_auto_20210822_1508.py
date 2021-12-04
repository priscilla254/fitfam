# Generated by Django 3.2.6 on 2021-08-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0010_auto_20210822_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='workout',
            field=models.CharField(choices=[('aerobics', 'aerobics'), ('Group class', 'Group class'), ('personal trainer', 'personal trainer')], default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plans',
            name='time',
            field=models.CharField(max_length=200),
        ),
    ]