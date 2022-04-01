"""
cree una funcion que tome los datos de un archivo externo los agrege a una lista y los imprima
"""
import os 

NOMBRE_ARCHIVO="datos.txt"
lista=[]
archivo=open(NOMBRE_ARCHIVO,"r")
for linea in archivo:
	lista.append(linea)

archivo.close()
print(lista[::])