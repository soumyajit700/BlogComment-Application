from django import forms
from django.contrib.auth.models import User
from .models import comment, Entry

class commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['hello','name', 'comment']


class postform(forms.ModelForm):
    class Meta:
        model = Entry
        fields= ['title', 'body', 'slug', 'publish']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
