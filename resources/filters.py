import django_filters
from .models import *
from django_filters import CharFilter


class FilesAdminFilter(django_filters.FilterSet):
    class Meta:
        model = FilesAdmin
        fields = ['subject', 'topic']
