import user
usuario=input("ingresar user:")
password=int(input("ingresar password:"))
user.login(usuario,password)
import time
import user
h=time.strftime("%I:%M:%S")
iduser=input("ingrese el iduser:")
user.listar(iduser,h)
import os
import user
Nuevo= "grupo.txt"
archivo=open(Nuevo,"r")
lista=[]
for linea in archivo:
    lista.append(linea)
archivo.close()
linea1=lista[0]
linea2=lista[1]
user.leer_registro(linea1,linea2)