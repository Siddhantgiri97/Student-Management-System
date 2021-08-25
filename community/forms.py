from django import forms
from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'thumb']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'thumb': forms.FileInput(attrs={'class': 'form-control'}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'thumb']
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'thumb': forms.FileInput(attrs={'class': 'form-control'}),
        }
