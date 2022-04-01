"""
Su compañero de clase no entiende la diferencia entre pasar parámetros por referencia y
por valor, haga un módulo punto1.py que tenga una función que reciba dos parámetros
(referencia y valor) e imprima cada parámetro, estos parámetros deben indicar lo que
significa cada uno para que cuando lo ejecute su compañero entienda cada uno.
"""
def punto_1(referencia,valor=17):
	print("el parametro valor:  es variable es el que toma diferentes valores:",referencia,)
	print("el parametro referencia:  es el que ya tiene asigando un valor:",valor)
	return