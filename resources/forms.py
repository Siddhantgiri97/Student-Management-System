from django import forms
from .models import FilesAdmin


class AddFilesAdmin(forms.ModelForm):
    class Meta:
        model = FilesAdmin
        fields = ['adminUpload', 'title', 'subject', 'topic']
        widgets = {
            'adminUpload': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
        }
