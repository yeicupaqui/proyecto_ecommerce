from django.forms import ModelForm
from .models import*
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password1','password2']

class Auto_Form(ModelForm):
    class Meta:
        model =   Autos
        fields =  ['nombre', 'kilometraje', 'comentarios' ,'marca',]

class Marca_Form(ModelForm):
    class Meta:
        model =   Marca
        fields =  ['nombre' ,] 