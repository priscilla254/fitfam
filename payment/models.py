from django.db import models
from gym.models import Member
from django.utils import timezone



class MemberPayment(models.Model):
    package_choices=(
        ('weekly','weekly'),
        ('monthly','monthly'),
        ('yearly','yearly'),
    )
    name=models.ForeignKey(Member,on_delete=models.CASCADE)
    package=models.CharField(max_length=200,choices=package_choices)
    payment_date=models.DateTimeField(timezone.now())
