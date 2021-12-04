from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Member,UserProfile

class MemberForm(ModelForm):
    class Meta:
        model= Member
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields='__all__'
        exclude=['user']