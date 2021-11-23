from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request):
    return render(request,'index.html')

@login_required(login_url="/")
def main(request):
    context={}
    context["usuario"]=request.user
    return render(request,'main.html',context)

def descripcion(request):
    context={}
    context["descripcion"]="Este proyecto web es parte de un taller de proyectos web con el lenguaje de programacion python y el framework django"
    return render(request,'descripcion.html',context)

@login_required(login_url="/")
def cerrar_sesion(request):
    auth.logout(request)
    return redirect("/")
    