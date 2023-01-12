from django.shortcuts import render, HttpResponse, redirect
from .models import Noticia1
from .forms import Nuevanoticia, CustomUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

html_base = """
    
"""

def home(request):
    return render(request,'core/home.html')

def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html')

def listado_noticias(request):
    noticias = Noticia1.objects.all
    data = {
        'Noticias':noticias
    }         
    return render(request,'core/listado_noticias.html',data)

def nueva_noticia(request):
    data = {
        'form':Nuevanoticia()
    }
    if request.method == 'POST':
        formulario = Nuevanoticia(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Publicado correctamente'
        else:
            data['mensaje'] = 'No ha funcionado'

    return render(request,'core/nueva_noticia.html', data)

def modificar_noticia(request, id):
    noticia = Noticia1.objects.get(id=id)
    data = {
        'form':Nuevanoticia(instance=noticia)
    }
    if request.method == 'POST':
        formulario = Nuevanoticia(data = request.POST, instance=noticia)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Modificado correctamente'
            data['form'] = formulario
        else:
            data['mensaje'] = 'No ha funcionado'
    return render(request,'core/modificar_noticia.html',data)

def eliminar_noticia(request, id):
    noticia = Noticia1.objects.get(id=id)
    noticia.delete()
    return redirect(to="lista")

def log_in(request):         
    return render(request,'registration/login.html')
    
def Log_out(request):
    logout(request)
    return redirect('home')

def registro(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect(to='home')
        else:
            data['mensaje'] = 'No ha funcionado'
    return render(request,'registration/registro.html', data)

