"""las excepciones ocuuren cuando se genera un error a la hora de ejecutar nuestro programa
con las excepciones podemos ocultar el error para que solo brinde la informacion adecuada,ya que cuando ocurre un error
aparece en que linea, y que tipo de error es por eso estan las excepciones 

"""
#ejemplo: 
try:
	#print(3/10) podemos dividir 3 entre 10
	print(3/0) #pero no podemos dividir 3 entre o
except Exception as ex: 
	print(ex)
	print("no es posible dividir entre 0")
finally:
	print("se termino")