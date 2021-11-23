from django.db import models
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from perfil.forms import *

# Create your views here.

def registro(request):
    if request.method == 'POST':
        if ("user" in request.POST.keys()) and ("pass1" in request.POST.keys()) and ("email" in request.POST.keys()) and (request.POST['pass1'] != "") and (request.POST['pass2'] != "") and (request.POST['user'] != "") and (request.POST['email'] != ""):
            user=request.POST['user']
            pass1=request.POST['pass1']
            mail=request.POST['email']
            pass2=request.POST['pass2']
            if pass1 == pass2:
                if User.objects.filter(username=user).exists():
                    context={}
                    context['mensaje1']='mensaje1'
                    return render(request,'registro/registro.html',context)
                if User.objects.filter(email=mail).exists():
                    context={}
                    context['mensaje2']='mensaje2'
                    return render(request,'registro/registro.html',context)
                newUser = User.objects.create_user(username=user,email=mail,password=pass1)
                newUser.save()
                profile = newUser.perfil
                profile.save()
                return redirect("/")
            else:
                context={}
                context['mensaje3']='mensaje3'
                return render(request,'registro/registro.html',context)
        else:
            context={}
            context['mensaje4']='mensaje4'
            return render(request,'registro/registro.html',context)
    
    return render(request,'registro/registro.html')

