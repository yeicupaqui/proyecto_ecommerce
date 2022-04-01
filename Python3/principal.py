import punto1 as pn
pn.punto_1("ejemplo nombre: yeily,luiz","ejemplo edad=17")
import punto2 as pn 
ap=[2]
pn.adoptar_p(ap)
print(ap)
import calculadora as cal
s,r,m,d=cal.calcular(2,10)
print("la suma es:",s)
print("la resta es:",r)
print("la multiplicacion es:",m)
print("la divicion es:",d)
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
