from .models import Trainer
from django.forms import ModelForm
from django import forms

class TrainerForm(ModelForm):
    class Meta:
        model=Trainer
        fields='__all__'