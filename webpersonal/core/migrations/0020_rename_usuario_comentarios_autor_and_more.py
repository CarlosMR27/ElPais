# Generated by Django 4.0.5 on 2023-01-28 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_comentarios_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentarios',
            old_name='usuario',
            new_name='autor',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='comentarios',
        ),
        migrations.AddField(
            model_name='comentarios',
            name='noticia',
            field=models.ManyToManyField(to='core.noticia'),
        ),
    ]
