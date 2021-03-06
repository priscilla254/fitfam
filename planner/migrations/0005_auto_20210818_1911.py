# Generated by Django 3.2.6 on 2021-08-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprogress',
            name='title',
            field=models.CharField(default=12, max_length=50),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='book',
            name='day',
        ),
        migrations.AddField(
            model_name='book',
            name='day',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myprogress',
            name='progress',
            field=models.TextField(),
        ),
    ]
