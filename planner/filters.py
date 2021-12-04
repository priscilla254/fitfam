import django_filters
from .models import *
from django_filters import CharFilter

class bookFilter(django_filters.FilterSet):
    day=CharFilter(field_name='day',lookup_expr='icontains') 
    class Meta:
        model=book
        fields=['day']