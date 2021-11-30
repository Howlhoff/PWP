from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import requests, json


# Create your views here.

def inicio(request):
    context = dict()
    context['lista'] = [1,2,3,4,5,6,7,8,9]
    return render(request,'index.html',context)

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
    
def query(request):
    url = requests.get("http://localhost:8001/")
    if url:
        text =  url.text
        data = json.loads(text)
        context = {}
        context['algo']=data
        return render(request,'query/query.html',context)
    else:
        return render(request,'query/query.html')