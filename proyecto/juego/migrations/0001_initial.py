# Generated by Django 3.2.8 on 2021-11-28 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='juego',
            fields=[
                ('id_juego', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, null=True, verbose_name='Nombre')),
                ('año', models.DateField(max_length=255, null=True, verbose_name='Fecha')),
                ('genero', models.CharField(max_length=100, null=True, verbose_name='Genero')),
                ('developer', models.CharField(max_length=255, null=True, verbose_name='Desarrollador')),
                ('publisher', models.CharField(max_length=255, null=True, verbose_name='Editor')),
                ('descripcion', models.CharField(max_length=255, null=True, verbose_name='Descripcion')),
                ('valoracion', models.IntegerField(null=True, verbose_name='Calificacion')),
                ('imagen', models.ImageField(default='juego_default.jpg', upload_to='juegos/')),
            ],
        ),
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='juego.juego')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
