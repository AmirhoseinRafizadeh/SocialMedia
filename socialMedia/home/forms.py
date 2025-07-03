from django import forms
from .models import Posts



class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['body']
