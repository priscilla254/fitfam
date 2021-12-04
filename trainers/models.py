from django.db import models
from django.db.models.fields import CharField, EmailField
from django.contrib.auth.models import User

class Trainer(models.Model):
    name=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    specialty=models.TextField()

    def __str__(self):
        return self.name
    
    class meta:
        ordering='name'

class TrainerSchedule(models.Model):
    name=models.ManyToManyField(Trainer)
    class_allocation=models.CharField(max_length=200)
    time=models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)+(self.class_allocation)