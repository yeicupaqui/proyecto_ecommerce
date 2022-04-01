"""
4.	Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades
 si este se le asigna como un porcentaje de su salario mensual que depende de su antigüedad 
 en la empresa de acuerdo con la siguiente tabla:
 Tiempo 	Utilidad 
Menos de 1 año  	5 % del salario 
1 año o más y menos de 2 años 	7% del salario 
2 años o más y menos de 5 años 	10% del salario 
5 años o más y menos de 10 años 	15% del salario 
10 años o mas 	20% del salario 
entrada
      -calcular cuanto recibe un trabajador si se le paga por la antiguedad 

proceso
      -si antiguedad <1 año entonces   su salario es el 5%
      -si su antiguedad es 1año hasta 2 años   su salario es de un 7%
      -si su antiguedad es de 2 años hasta 5 su salario es de 10%
      -si su antiguedad es de 5 años hasta 10 su salario es el 15%
      -si su antiguedad es de 10 años o mas su salario es el 20%
salida
imprimir ingrese su año de antiguedad
imprimir su salario mensual
imprimir su pago es 

#prueba de escritorio
#antiguedad             salario       pago
#1                       10000         200000   
#7                       30000         450000
#9                       25000         375000
#2                       17000         340000
"""
antiguedad=int(input("ingrese su años de antiguedad:"))
sumamensual=int(input("ingrese su salario mensual:"))

if antiguedad<1:
	utilidad=sumamensual*0.05
	
elif antiguedad >1 and antiguedad <2:
	utilidad=sumamensual*7

elif antiguedad >2 and antiguedad<5:
	utilidad=sumamensual*10
elif antiguedad >5 and antiguedad<10:
	utilidad=sumamensual*15
else:
	utilidad=sumamensual*20	
    
print("su pago es:",utilidad)
