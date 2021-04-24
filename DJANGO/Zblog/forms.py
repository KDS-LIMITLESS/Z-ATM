from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Comment


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'email', 'body'] 

