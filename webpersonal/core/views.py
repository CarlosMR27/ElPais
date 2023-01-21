from django.shortcuts import render, HttpResponse, redirect
from django.contrib import admin
from .models import Noticia
from .forms import Nuevanoticia, CustomUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Q
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.

html_base = """
    
"""
#-----------------------------------------------------------------------------------------------#
                                            #Admin

#-----------------------------------------------------------------------------------------------#
                                            #Vistas de post

def home(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.all().order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda)
        ).order_by('-creacion').distinct()
    return render(request,'core/home.html',{"noticias": noticias})

def actualidad(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 1).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 1)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/actualidad.html',{"noticias": noticias})

def cronica(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 2).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 2)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/cronica.html',{"noticias": noticias})

def internacionales(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 3).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 3)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/internacionales.html',{"noticias": noticias})

def deportes(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 4).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 4)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/deportes.html',{"noticias": noticias})

def insolito(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 5).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 5)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/insolito.html',{"noticias": noticias})

def tendencias(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 6).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 6)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/tendencias.html',{"noticias": noticias})

def farandula(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 7).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 7)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/farandula.html',{"noticias": noticias})

def tecnologia(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 8).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 8)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/tecnologia.html',{"noticias": noticias})

def detalle_noticia(request,slug):
    noticias = Noticia.objects.get(
        slug = slug
    )
    similares = Noticia.objects.filter(seccion = noticias.seccion).exclude(titulo = noticias.titulo).order_by('-creacion')[:4]
    recomendados = Noticia.objects.exclude(seccion = noticias.seccion).order_by('-creacion')[:6]
    return render(request,'core/publicacion.html',{"noticias": noticias, "similares": similares, "recomendados": recomendados})
#-----------------------------------------------------------------------------------------------#
                                            #Vistas Info

def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html')

#-----------------------------------------------------------------------------------------------#
                    #Vistas de ingreso, modificación y eliminación de post

@permission_required('core/noticia1.view')
def listado_noticias(request):
    noticias = Noticia.objects.all().order_by('-update')
    data = {
        'Noticias':noticias
    }         
    return render(request,'core/listado_noticias.html',data)

@permission_required('core/noticia1.add')
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

@permission_required('core/noticia1.change')
def modificar_noticia(request, id):
    noticia = Noticia.objects.get(id=id)
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

@permission_required('core/noticia1.delete')
def eliminar_noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    noticia.delete()
    return redirect(to="lista")

#-----------------------------------------------------------------------------------------------#
                            #Vistas de login, logout, register

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
            group = Group.objects.get(name='Lector')
            user.groups.add(group)
            login(request,user)
            return redirect(to='home')
        else:
            data['mensaje'] = 'No ha funcionado'
    return render(request,'registration/registro.html', data)

#-----------------------------------------------------------------------------------------------#
