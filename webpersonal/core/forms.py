from django import forms
from django.forms import ModelForm
from.models import Noticia, Comentarios, User_personalizado, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Modelos de formularios

class Nuevanoticia(ModelForm):
    
    class Meta:
        model = Noticia
        fields = ['titulo', 'slug', 'portada', 'pie_portada', 'cuerpo',  'enlace', 'seccion','es_portada']


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

#class Profileform(forms.ModelForm):
    #first_name = forms.CharField()
    #last_name = forms.CharField()

    #class Meta:
        #model = User_personalizado
        #fields = ('fist_name', 'last_name', 'profilepic')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comentarios
        fields = ('comentario',)