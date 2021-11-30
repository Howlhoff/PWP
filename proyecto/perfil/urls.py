from django.urls import path
from perfil.views import *

urlpatterns = [
    path("",perfilx),
    path("editar",editar_perfil),
    path("contrasena",password_change),  
]