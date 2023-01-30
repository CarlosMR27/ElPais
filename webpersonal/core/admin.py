from django.contrib import admin
from .models import Noticia, Seccion, User_personalizado, Autor, Editor, Comentarios

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'seccion', 'autor','creacion','update']
    search_fields = ['titulo', 'seccion']
    list_filter = ['seccion','creacion','autor']
    list_per_page = 15


# Register your models here.
admin.site.register(Seccion)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(User_personalizado)
admin.site.register(Autor)
admin.site.register(Editor)
admin.site.register(Comentarios)

