from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse,Http404
from django.core.paginator import Paginator
from .models import  *
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


@login_required
def carros(request):

    autos = Autos.objects.all()

    context  = {'autos' : autos}

    return render(request, 'carros.html', context )









# Create your views here.
def cerrar_secion(request):
     logout(request)
     return redirect('login')



def nuevo_auto(request):
    data={
        'form':Auto_Form()
    }
    if request.method == 'POST':
        form = Auto_Form(request.POST, request.POST, request.FILES)
        if form.is_valid():
            form.save()

        else:
            data["from"]=form

    return render(request,'auto/nuevo_auto.html',data)


def lista_auto(request):

    auto = Autos.objects.all()
    marca = Marca.objects.all()

    data = {'auto': auto, 'marca':marca}

    return render(request,'auto/lista_auto.html', data)


