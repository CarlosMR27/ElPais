from django import forms
from django.forms import ModelForm
from.models import Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Modelos de formularios

class Nuevanoticia(ModelForm):
    
    class Meta:
        model = Noticia
        fields = ['titulo', 'slug', 'cuerpo', 'imagen', 'enlace', 'seccion']


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']