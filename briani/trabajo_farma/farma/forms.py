from django.forms import ModelForm
from .models import*
from .models import Producto
from .models import Categoria


class Producto_Form(ModelForm):
    class Meta:
        model =   Producto
        fields =  ['codigo', 'nombre', 'precio' ,'especificaciones', 'categoria']      

class Categoria_Form(ModelForm):
    class Meta:
        model =   Categoria
        fields =  [ 'codigo','nombre'] 