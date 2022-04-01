from django.shortcuts import render
from .models import*
from .forms import Auto_Form
from .forms import Marca_Form
# Create your views here.
def main(request):
    context = {}
    return render(request,'auto/main.html', context)

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


