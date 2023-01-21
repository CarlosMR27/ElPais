from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Seccion(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Noticia(models.Model):
    titulo = models.CharField(max_length=(300), blank=False, null= False)
    slug = models.CharField(max_length=(50), blank=False, null= False)
    cuerpo = RichTextField()
    imagen = models.ImageField(upload_to='noticia/%Y/%m/%d')
    creacion = models.DateTimeField(auto_now_add=True)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    enlace = models.CharField(max_length=(200),blank=True, null= True)
    update = models.DateTimeField(auto_now=True)