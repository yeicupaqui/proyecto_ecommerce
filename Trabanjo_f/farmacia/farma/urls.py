from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('agregar_producto/',views.agregar_producto, name='agregar_producto'),

]