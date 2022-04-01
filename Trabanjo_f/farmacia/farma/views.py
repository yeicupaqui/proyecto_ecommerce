from django.shortcuts import render
from .models import  *
from .forms import Producto_Form
#from .forms import agregar_producto_form
# Create your views here.

def main(request):
    context = {}
    return render(request,'farma/main.html', context)


def agregar_producto(request):
     data = {
          'form':Producto_Form()
     }
     if request.method == 'POST':
          form = Producto_Form(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               message.success(request, 'Producto Agregado ')
               
          else:
               data["from"] = form     
               
     return render(request,'farma/agregar_producto.html', data )


"""
def lista_producto(request):
    lista = Producto.objects.filter()
    return render(request,'farma/lista_producto.html', locals())

def lista_categoria(request):
    lista = Categoria.objects.filter()
    return render(request,'farma/lista_categoria.html', locals())

"""