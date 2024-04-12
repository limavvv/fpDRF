from django_filters import rest_framework as filters
from .models import *

class MovieFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title',lookup_expr='icontains') 

    class Meta:
        model = Movie
        fields = {
            'genres': ['exact']
        }


class ActorFilter(filters.FilterSet):
    full_name = filters.CharFilter(field_name='last_name', lookup_expr='icontains')

    class Meta:
        model = Actor
        fields = ('first_name',)