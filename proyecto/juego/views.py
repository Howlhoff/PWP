from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url='/')
def juegoperfil(request):
    context = dict()
    context['juego']=juego.objects.all()
    if request.user is not None:
        context['usuario'] = request.user
    if request.method == 'POST':
        form = formComentario(request.POST or None)
        if form.is_valid():
            contenido = request.POST.get('contenido')
            texto = comentario.objects.create(game = juego, user = request.user, texto = contenido)
            texto.save()
            if texto:
                lista = []
                lista.append(texto)
                context['comentarios']=lista
                return render(request,"perfiljuego/perfiljuego.html",context)
            else:
                return redirect(juego.get_absolute_url())
    else:
        form = formComentario()
        context['form'] = form
        return render(request,"perfiljuego/perfiljuego.html",context)
