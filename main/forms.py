from django.contrib.auth.models import User
from .models import Post, Profile, Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email       = forms.EmailField()
    class Meta:
        model   = User
        fields  = ['username', 'email', 'password1', 'password2']

class UserUpdate(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

