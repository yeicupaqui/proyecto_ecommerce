"""
2.	Cual es la nota final de un alumno si esta se obtiene de la siguiente forma
•	Quiz 10%
•	Trabajo 15%
•	Exposicion 25%
•	Exmane Final 50%

entrada
     -nota final de un alumno

proceso
      -declarar variables
      -quiz
      -trabajo
      -exposicion
      -examne final
salida
imprimir la nota final del estudiante 

#prueba de escritorio
nombre   nota del quiz    nota del trabajo    nota exposicion    nota examen final    la nota final del estudiante es 
yeily     3.2                2.4                  3.2               4.3                  3.63
juan       4.2                2.1                  4.5              1.2                  2.46
pedro      1.2                 2.0                 2.3               3.2                 2.5
"""
nombre=input("ingrese su nombre:")
quiz=float(input("ingrese la nota de quiz:"))
trabajo=float(input("ingrese la nota de trabajo:"))
exposicion=float(input("ingrese la nota de exposicion:"))
examenfinal=float(input("ingrese la nota de examen final:"))

nq=quiz*10/100
nt=trabajo*15/100
ne=exposicion*25/100
nf=examenfinal*50/100
tn=nq+nt+ne+nf

print (nq)
print (nt)
print (ne)
print (nf)

print("la nota final de estudiante",nombre,"es:",tn)