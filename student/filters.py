import django_filters
from .models import *
from result.models import *
from exam.models import *


class ExamResultFilter(django_filters.FilterSet):
    class Meta:
        model = ExamResult
        fields = ['student__stu_class', 'exam']
        exclude = ['marks_obtained']
        
