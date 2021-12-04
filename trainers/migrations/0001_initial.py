# Generated by Django 3.2.6 on 2021-08-25 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('specialty', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainerSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_allocation', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('name', models.ManyToManyField(to='trainers.Trainer')),
            ],
        ),
    ]
