from django.shortcuts import render
from .forms import Producto_Form
from .forms import Categoria_Form
# Create your views here.

def main(request):
    context = {}
    return render(request,'farma/main.html', context)

def nuevo_producto(request):
     data = {
          'form':Producto_Form()
     }
     if request.method == 'POST':
          form = Producto_Form(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, 'Producto Agregado ')
               
          else:
               data["from"] = form     
               
     return render(request, 'farma/nuevo_producto.html',data)


def lista_produtos(request):
     producto = Producto.objects.all()
     categorias = Categoria.objects.all()
      
          
     data = {'producto' : producto,'categorias' :categorias}
     return render(request,'farma/lista_produtos.html', data)
