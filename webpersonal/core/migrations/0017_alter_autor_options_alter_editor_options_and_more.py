# Generated by Django 4.0.5 on 2023-01-26 05:38

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_user_personalizado_profilepic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='editor',
            options={'verbose_name': 'Editor', 'verbose_name_plural': 'Editores'},
        ),
        migrations.AlterModelOptions(
            name='noticia',
            options={'verbose_name': 'Noticia', 'verbose_name_plural': 'Noticias'},
        ),
        migrations.AlterModelOptions(
            name='seccion',
            options={'verbose_name': 'Sección', 'verbose_name_plural': 'Secciones'},
        ),
        migrations.AlterModelOptions(
            name='user_personalizado',
            options={'verbose_name': 'Usuario personalizado', 'verbose_name_plural': 'Usuarios personalizados'},
        ),
        migrations.AlterField(
            model_name='user_personalizado',
            name='profilepic',
            field=models.ImageField(default='inicio_edit.png', upload_to=core.models.User_personalizado.user_directory_path),
        ),
    ]