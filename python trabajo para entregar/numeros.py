
"""
7.	Leer número enteros hasta que digiten 0 
y determinar el promedio de los números leídos que hayan sido positivos e informar 
cual fue el mayor número dado por el usuario.

analisis del algoritmo

entrada
      -digite un numero


proceso
      -ciclo si numero es diferente a 0
      -numero es mayor de 0 es positivo
            -contador de numeros positivos
       -si numero es mayor al mayor
       -si no es negativo
salida
      -imprimir el promedio de numeros positivos
      -imprimir el numero mayor solamente de los numeros positivos

prueba de escritorio

#digite el numero               promedio numeros positivos       el numero mayor
5
8
12
-3
28
0                                p=5+8+12+28/4   ->13,25                     28

"""
conteo=0
suma=0
numero=1
nummayor=0
while numero !=0 :
	numero=int(input("digite el numero:"))
	if numero >0:
		suma=suma+numero
		conteo=conteo+1
		if numero>nummayor:
			nummayor=numero
		else:
			pass
	else:
		pass
print("el promedio de los numeros es:",suma/conteo)
print("el numero mayor de los positivos es:",nummayor)
