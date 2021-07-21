from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta: #keeps the fields together. So will affect the User model, and the fields.
        model = User
        fields = ['username', 'email', 'password1', 'password2']
