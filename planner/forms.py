from planner.models import book,Plans
from django import forms
from django.forms import ModelForm

class BookForm(forms.ModelForm):
    class Meta:
        model=book
        fields=['day','name','workout','time']
        

class PlansForm(forms.ModelForm):
    class Meta:
        model=Plans
        fields='__all__'
        
        


