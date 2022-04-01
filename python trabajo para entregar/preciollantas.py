"""
1.	Calcular el total que una persona debe pagar en un llantero, 
si el precio de cada llanta es de $800 si se compran menos de 5 llantas
y de $700 si se compran 5 o más.

entrada
      -precio que se debe pagar en un llantero
      -si se compra-5 el precio es de 800
      -si se compra 5+ el precio 700 
proceso
      -si llantas >=5 el precio de pagar es llantas*700
      sino  el precio a pagar es llantas*800
salida
imprimir el valor a pagar si compra menos de 5 llantas
imprimir el valor a pagar si son 5 llantas o mas.

#prueba de escritorio
#llamtas                si compra 5 o mas          si compra menos de 5                      total a pagar
#4                                                    800                            3200
#7                              700                                                   4900

"""

llantas=int(input("ingrese el valor de llantas a comprar:"))

if llantas>=5:
	print("el valor a pagar es:",llantas*700)
else:
	print("el valor a pagar es:",llantas*800)