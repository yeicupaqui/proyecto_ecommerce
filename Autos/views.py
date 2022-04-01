from django.shortcuts import render

from .models import  Autos

from .forms import Autos_Form

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib import messages

def vautos(request):
         
     return render(request, 'autos/ventas.html')



def registrar_usuario(request):

     form= CreateUserForm()
     if request.method == 'POST':
          form =CreateUserForm(request.POST)
          if form.is_valid():
               form.save()
               user= form.cleaned_data.get('username')
               messages.success(request, 'Se a Creado con exito' + user  )
               return redirect(logins)

     context ={'form':form}
     return render(request, 'store/registrar_usuario.html', context)



def logins(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          user =authenticate(request, username=username, password=password)
          if user is not None:
               login (request, user)
               return redirect('checkout')
          else:
                    messages.info(request, 'el usuario es incorrecto ')
     context ={}
     return render(request,'store/logins.html', context)  


def cerrar_secion(request):
     logout(request)
     return redirect('store')

     
#PRODUCTOS
     

def añadir_autos(request):
     data = {
          'form':Autos_Form()
     }
     if request.method == 'POST':
          form = Autos_Form(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, 'Agregado ')
               
          else:
               data["from"] = form     
               
     return render(request, 'autos/añadir_autos.html', data )

def lista_autos(request):
     producto = Autos.objects.all()
     data = {'autos' : autos}
     return render(request,'autos /lista_produtos.html', data)


def editar_autos(request, id ):
     productos = get_object_or_404(Producto, id=id)

     data = {
          'form':Autos_Form(instance=productos)
     }
     if request.method == 'POST':
          form = Autos_Form(data=request.POST, instance=productos, files=request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, ' Modificado ')
               return redirect  ("lista" )
               
          data ['form'] = 'form'

     return render(request, 'store/modificar.html',data ) 



def elimanar_autos(request, id):
     autos = get_object_or_404(Autos, id=id)
     autos.delete()
     messages.success(request, 'Producto Eliminado ')
     return redirect  ("lista" )



def ver_detalle(request, id):
    

     object = Producto.objects.get(id = id)

     return render(request, 'store/detalle.html', locals() )



#CATEGORIA
def lista_marca(request):
     data = {
          'form':Marca_Form()
     }
     if request.method == 'POST':
          form = Marca_Form(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, ' Agregado ')
               
          else:
               data["from"] = form     
               
     return render(request, 'store/nueva_marca.html', data )


def nueva_marca(request):
     categoria = Marca.objects.all().order_by('-id')
     data = {'categoria' : categoria}
     return render(request,'store/lista_marca.html', data)
     

def editar_marca(request, id ):
     categoria = get_object_or_404(Categoria, id=id)

     data = {
          'form':Marca_Form(instance=categoria)
     }
     if request.method == 'POST':
          form = Marca_Form(data=request.POST, instance=categoria, files=request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, 'Marca Modificado ')
               return redirect  ("listar" )
               
          data ['form'] = 'form'

     return render(request, 'store/modificarcate.html',data ) 

def elimina_marca(request, id):
     categoria = get_object_or_404(Categoria, id=id)
     categoria.delete()
     messages.success(request, 'Marca Eliminado ')
     return redirect  ("listar")
