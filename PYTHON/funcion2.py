def convertir_segundos(segundos):
	minutos=segundos/60
	hora=minutos/60
	return minutos, hora

m,h= convertir_segundos(6000)
print("hora=",h)
print("minutos=",m)