# Generated by Django 3.2.6 on 2021-08-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_alter_userprofile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='profile_pics'),
        ),
    ]
