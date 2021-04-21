from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    firstName = forms.CharField(max_length=15, required=True)
    lastName = forms.CharField(max_length=15, required=True)
    otherNames = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['firstName', "lastName", "otherNames", "email"]
