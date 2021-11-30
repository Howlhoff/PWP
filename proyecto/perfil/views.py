from django.shortcuts import redirect, render
from django.contrib import auth,messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from perfil.forms import *

@login_required(login_url="/")
def perfilx(request):
    context={}
    if User.objects.filter(username = request.user).exists() and perfil.objects.filter(n_usuario = request.user).exists():
        user = User.objects.get(username=request.user)
        per = perfil.objects.get(n_usuario=request.user)
        context["usuario"]=user.username
        context["ciudad"]=per.ciudad
        context["pais"]=per.pais
        context["descripcion"]=per.descripcion
        context["imagen"]=per.imagen
        context["comentarios"]=[1,2,3,4,5,6]
        return render(request,'perfil/perfil.html',context)
    else:
        context["usuario"]=request.user
        return render(request,'perfil/perfil.html',context)

@login_required(login_url="/")
def editar_perfil(request):
    if request.method == "POST":
        form1 = formUser(request.POST or None, instance = request.user)
        form2 = formPerfil(request.POST or None,request.FILES, instance = request.user.perfil)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('/perfil')
    form1 = formUser(instance = request.user)
    form2 = formPerfil(instance = request.user.perfil)
    context = {"usuario":request.user,"form1":form1,"form2":form2}
    return render(request,'perfil/editar.html',context)

@login_required(login_url="/")
def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('/perfil')
        else:
            context = {}
            context['error'] = 'Ha ocurrido un error'
            return render(request,'perfil/contraseña.html',context)
    else:
        form = PasswordChangeForm(request.user)
        context=dict()
        context['usuario'] = request.user
        context['form'] = form
        return render(request,'perfil/contraseña.html',context)
    