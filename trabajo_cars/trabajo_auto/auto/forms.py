from django import forms
from django.forms import ModelForm
from .models import*


class Auto_Form(ModelForm):
    class Meta:
        model =   Autos
        fields =  ['nombre', 'kilometraje', 'comentarios' ,'marca',]

class Marca_Form(ModelForm):
    class Meta:
        model =   Marca
        fields =  ['nombre' ,] 