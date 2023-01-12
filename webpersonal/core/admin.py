from django.contrib import admin
from .models import Noticia1, Seccion

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'seccion']
    search_fields = ['titulo', 'seccion']
    list_filter = ['seccion','creacion']


# Register your models here.
admin.site.register(Seccion)
admin.site.register(Noticia1, NoticiaAdmin)
