from django.db import models
from django.contrib.auth.models import User

class juego(models.Model):
    id_juego=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=255,verbose_name="Nombre",blank=False,null=True)
    año=models.DateField(max_length=255,verbose_name="Fecha",blank=False,null=True)
    genero=models.CharField(max_length=100,verbose_name="Genero",blank=False,null=True)
    developer=models.CharField(max_length=255,verbose_name="Desarrollador",blank=False,null=True)
    publisher=models.CharField(max_length=255,verbose_name="Editor",blank=False,null=True)
    descripcion=models.CharField(max_length=255,verbose_name="Descripcion",blank=False,null=True)
    valoracion=models.IntegerField(verbose_name="Calificacion",blank=False,null=True)
    imagen=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)


class comentario(models.Model):
    id_juego=models.ForeignKey(juego,on_delete=models.CASCADE,blank=True,null=True)
    n_usuario=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    texto=models.CharField(max_length=1000,verbose_name="Comentario",blank=False,null=True)
    valoracion=models.IntegerField(verbose_name="Valoracion",blank=False,null=True)
