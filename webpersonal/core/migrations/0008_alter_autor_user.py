# Generated by Django 4.0.5 on 2023-01-24 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_autor_editor_user_personalizado_delete_perfil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user_personalizado'),
        ),
    ]
