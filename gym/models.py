from django.db import models
import datetime
from django.utils import timezone
from django.db.models.fields import EmailField
from django.urls import reverse
from django.contrib.auth.models import User

class Member(models.Model):
    GENDER_CHOICES=(
        ('male','male'),
        ('female','female'),
    )
    FEE_STATUS = (
    ('paid', 'Paid'),
    ('pending', 'Pending'),
    )
    STATUS=(
        ('active','active'),
        ('inactive','inactive')
    )
    SUBSCRIPTION_TYPE=(
    ('daily','daily'),
    ('weekly','weekly'),
    ('monthly','monthly'),
    ('yearly','yearly')
    )

    
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=200,blank=True,unique=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=200,choices=GENDER_CHOICES)
    date_joined=models.DateField(null=True,blank=True)
    status=models.CharField(max_length=200,choices=STATUS)
    subscription=models.CharField(max_length=200,choices=SUBSCRIPTION_TYPE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    
    email=models.EmailField(null=True)
    gym_goal=models.CharField(max_length=200,null=True)
    profile_photo=models.ImageField(null=True,blank=True,default='default.png',upload_to='profile_pics')
    def __str__(self):
        return self.user.username


class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Services(models.Model):
    CLASS_CHOICES=(
        ('aerobics','aerobics'),
        ('circuit class','circuit class'),
        ('solo training','solo training'),
    )
    title=models.CharField(max_length=200,choices=CLASS_CHOICES)
    Description=models.TextField()
    image=models.ImageField(verbose_name="image",upload_to="services")


