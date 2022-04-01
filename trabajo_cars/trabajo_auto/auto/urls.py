from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('auto',views.nuevo_auto, name='auto'),
    path('lista/',views.lista_auto, name='lista'),

]