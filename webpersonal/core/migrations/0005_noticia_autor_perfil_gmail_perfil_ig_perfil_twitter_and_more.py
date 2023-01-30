# Generated by Django 4.0.5 on 2023-01-22 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_perfil_delete_userdefinido'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='gmail',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='ig',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='twitter',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='enlace',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
