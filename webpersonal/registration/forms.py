from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationEmail(UserCreationForm):
    email=forms.EmailField(required=True,help_text="es un campo requerido con formato valido para correo")

    class Meta:
        model=User
        fields=("username","email","password1","password2")

