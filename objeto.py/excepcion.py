#las excepciones ocuuren cuando se genera un error a la hora de ejecutar nuestro programa 
try:
	print(6/13)
except Exception as ex:
	print(ex)
	print("no es posible dividir entre 0")
finally:
	print("se termino")