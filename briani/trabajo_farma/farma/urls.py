from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('producto/',views.nuevo_producto, name='producto'),
    #path('lista/',views.lista_produtos, name='lista'),
]