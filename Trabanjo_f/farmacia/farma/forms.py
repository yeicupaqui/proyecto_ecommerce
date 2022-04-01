from django.forms import ModelForm
from .models import*
from django import forms

class Producto_Form(ModelForm):
    class Meta:
        model =   Producto
        fields =  ['codigo', 'nombre', 'precio' ,'especificaciones', 'categoria']      
