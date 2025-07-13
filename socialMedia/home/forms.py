from django import forms
from .models import Posts, comments



class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['body']



class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }