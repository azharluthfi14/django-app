from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from .models import *
from .validators import validate_email_unique


class form_user_create(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)
    email = forms.CharField(required=True, label='Email adress', validators=[
                            validate_email_unique])
    password1 = forms.CharField(required=True, label='Password')
    password2 = forms.CharField(required=True, label='Password confirmation')

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]

    username.widget = forms.TextInput(
        attrs={'class': 'signupForm', 'placeholder': 'Enter your username.'})
    email.widget = forms.EmailInput(
        attrs={'class': 'signupForm', 'placeholder': 'Enter your valid email addres.', 'data-placement': 'top', 'data-content': 'Must be a valid e-mail address'})
    password1.widget = forms.PasswordInput(
        attrs={'class': 'signupForm', 'placeholder': '●●●●●●●●', 'data-placement': 'bottom'})
    password2.widget = forms.PasswordInput(
        attrs={'class': 'signupForm', 'placeholder': '●●●●●●●●'})


class form_user_update(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class user_update_profile(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['image']
    image.widget = forms.FileInput(attrs={'class': 'image-upload'})