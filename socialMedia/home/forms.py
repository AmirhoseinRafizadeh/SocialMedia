from django import forms
from .models import Posts



class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['body']
