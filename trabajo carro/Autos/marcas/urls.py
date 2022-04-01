from django.contrib.auth import login
from django.urls import path
from django.contrib.auth.decorators import login_required
from  .import views 



urlpatterns = [

    path('',views.carros, name="carros"),
    path('cerrar/', views.cerrar_secion, name='cerrar' ),

    
    











]