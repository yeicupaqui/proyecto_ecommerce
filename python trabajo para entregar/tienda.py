#6.	Suponga que tiene usted una tienda y desea registrar las ventas en una computadora. 
# Diseñe un programa que lea por cada cliente, el monto total de su compra. 
#Al final del día escriba la cantidad total de las ventas y el número de clientes atendidos.
"""analisis del algoritmo
entradas
      -nombre del cliente
      total de su compra
proceso 
      -crear un ciclo de condiciom verdadera crear un varisble centinela
      -suma de todas las compras a traves de un acumulador
      -suma de todos los clientes mediante un acumulador
salida
      -imprimo el total de compras
      -imprimo el total de clientes
prueba de escritorio
#cliente            compra total de cliente --mensaje(desea salir si/no)         total de compras            total de clientes
nombre 1                $35.000                      no
nombre2                 $#48.300                     no           
nombre 3                 $54.800                      si                       $138.000                         3
"""
a="no"
ccliente=0
acum=0
while a == "no":
	cliente=input("ingresar cliente:")
	ccliente=ccliente+1
	compra=int(input("valor de la compra:"))
	acum=acum+compra
	a=str(input("desea salir si / no:"))
print("la cantidad de clientes en el dia fueron:",ccliente)
print("el total de todas las compras en el dia son:",acum)