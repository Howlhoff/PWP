from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        if ("user" in request.POST.keys()) and ("pass" in request.POST.keys()) and (request.POST['user'] != "") and (request.POST['pass'] != ""):
            user = auth.authenticate(username=request.POST['user'],password=request.POST['pass'])
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect("/main")
            else:
                context={}
                context["error1"]="error"
                return render(request,'login/login.html',context)
        else:
            context={}
            context["error2"]="error"
            return render(request,'login/login.html',context)

    return render(request,'login/login.html')
