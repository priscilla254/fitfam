from django.db import models

class Remote_bookings(models.Model):
    name=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=50)
    email=models.EmailField()
    location=models.CharField(max_length=200)
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
