"""3Una compañía dedicada al alquiler de automóviles cobra un monto fijo de $300.000
para los primeros 300 km de recorrido.
Para más de 300 km y hasta 1000 km, cobra un monto adicional de $15.000 por cada kilómetro en exceso sobre 300.
Para más de 1000 km cobra un monto adicional de $ 10.000 por cada kilómetro en exceso sobre 1000. 
Diseñe un algoritmo que determine el monto a pagar por el alquiler de un vehículo.

entrada
      -el monto a pagar poe el alquiler de un vehiculo

proceso
      -si km recorridos es <=300 el monto a pagar es de 300000
      -si km reccorridos es >300 hasta 1000 tiene un cobro adicional de 15000
      -si km recorridos es >1000 tiene un cobro de 10000

salida
imprimir los kilometros recorridos
imprimir el monto a pagar es de 
#prueba de escritorio
#km rrecorridos                     monto a pagar 
#400                                    1800000
#500                                    3300000
#600                                    4800000            
#300                                    300000
#1000                                  10800000
"""
km_recorridos=float(input("ingrese km recorridos:"))
monto_pagar=0
monto_fijo=300000
if km_recorridos<=300:
	monto_pagar=monto_fijo
if km_recorridos>300 and km_recorridos<=1000:
	monto_pagar=monto_fijo+(km_recorridos-300)*15000
if km_recorridos>1000:
	monto_pagar=monto_fijo+700*15000+(km_recorridos-1000)*10000
print("el monto a pagar es:",monto_pagar)