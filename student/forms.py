from django import forms
from .models import Student, Notification


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name': 'Name',
            'stu_class': 'Class',
            'rollNo': 'Roll No',
            'batch': 'Batch',
            'address': 'Address',
            'contact': 'Contact No',
            'email': 'E-mail',
            'image': 'Profile',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'stu_class': forms.Select(attrs={'class': 'form-control'}),
            'rollNo': forms.TextInput(attrs={'class': 'form-control'}),
            'batch': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),

        }


class AddNotification(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['text']
        labels = {
            'text': 'Notification',
        }
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }
