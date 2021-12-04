import django_filters
from .models import *
from django_filters import CharFilter

class MemberFilter(django_filters.FilterSet):
    name=CharFilter(field_name='name',lookup_expr='icontains') 
    class Meta:
        model=Member
        fields=['name']
        

