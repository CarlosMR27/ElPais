# Generated by Django 4.0.5 on 2023-01-24 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_noticia_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_personalizado',
            name='profilepic',
            field=models.ImageField(default='inicio.png', upload_to='profile_pics/user.username'),
        ),
    ]
