from django import forms
from .models import Exam


class ExamForm(forms.ModelForm):

    class Meta:
        model = Exam
        fields = ['subject', 'topic', 'total_marks', 'student']
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'student': forms.CheckboxSelectMultiple(),
            'total_marks': forms.TextInput(attrs={'class': 'form-control'}),

        }
