"""
5.	Suponga que se tiene un conjunto de calificaciones de un grupo de 40 alumnos.
Realizar un algoritmo para calcular el promedio de las calificaciones e 
informe la calificación más baja de todo el grupo.
entrada
      -las calificaciones de 40 alumnos
      -el promedio de las calificaciones
      -la calificacion mas baja de todo el gupo
proceso
     -usar el ciclo for para ir ingresando las notas
     -sumar las notas para sacar el promedio
     -si la nota <calificacionbaja
              calificacionbaja=nota

salida
imprimir ingrese la calificacion
imprimir el promedio de las calificaciones
imprimir la calificacion mas baja es

prueb de escritorio
ingrese la calificacion         el promedio de las calificaciones         la calificacion mas baja
3.2
1.0
4.3
3.2
1.0   
5.0
4.3
2.3
1.2
4.3
                           promedio=5.96                                     1.0
"""
nota=0
suma=0
promedio=0
baja=1.0

for nota in range (10):
	nota=float(input("ingrese la calificacion:"))
	suma+=nota
	promedio=suma/5
if nota<baja:
	baja=nota
print("el promedio de las calificaciones es:",promedio)
print("la calificacion baja es:",baja)