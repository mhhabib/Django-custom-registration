from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'joeschmoe', 'name': 'username'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'joeschmoe@xyz.com', 'name': 'email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
