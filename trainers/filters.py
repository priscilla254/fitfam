import django_filters
from .models import *
from django_filters import CharFilter

class TrainerFilter(django_filters.FilterSet):
    name=CharFilter(field_name='name',lookup_expr='icontains') 
    class Meta:
        model=Trainer
        fields=['name']