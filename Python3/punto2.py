"""Cree un módulo punto2.py y cree una función adoptarPerrito
que reciba un parámetro numeroperritos y que sume +1 al valor enviado,
aplique el paso por referencia para que la variable enviada a la función cambie al nuevo valor generado 
en la función e imprima el resultado final.
"""
def adoptar_p(numerop):
	for i, n in enumerate(numerop):
		numerop[i] +=1
		