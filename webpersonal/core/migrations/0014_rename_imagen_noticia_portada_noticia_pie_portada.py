# Generated by Django 4.0.5 on 2023-01-25 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_user_personalizado_es_autor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='imagen',
            new_name='portada',
        ),
        migrations.AddField(
            model_name='noticia',
            name='pie_portada',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
