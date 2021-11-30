from django.urls import path
from main.views import *

urlpatterns = [
    path("",inicio),
    path("main/",main),
    path("descripcion/",descripcion),
    path("cerrar_sesion/",cerrar_sesion),
    path('buscador/',query),
]