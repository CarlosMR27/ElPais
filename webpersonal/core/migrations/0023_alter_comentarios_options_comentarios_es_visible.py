# Generated by Django 4.0.5 on 2023-01-28 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_comentarios_noticia'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentarios',
            options={'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
        migrations.AddField(
            model_name='comentarios',
            name='es_visible',
            field=models.BooleanField(default=True),
        ),
    ]
