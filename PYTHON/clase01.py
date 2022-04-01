"""
crear una funcion que reciba el dato
de tipo de estudio el nombre del estudiante
y retorne un en que tipo de estudio  se encuentra
e imprima el nombre ejemplo
tipo
tec=tecnico 6 meses de etapa lectiva y 6 de practica
teg=tecnologo 18 meses de etapa legtiva y 6 de practica
com=complementario el tiempo en horas(40 horas -60 hras- 120 horas)
"""
def tipo_estudio(tipo,nombre,duracion):
	if tipo=="tec":
		tipo="tecnico"
		n=nombre
		dur=duracion
		return tipo,n,dur
	elif tipo =="tgo":
		tipo="tecnologo"
		n=nombre
		dur=duracion
		return tipo,n,dur
	else:
		tipo="complemento"
		n=nombre
		dur=duracion
		return tipo,n,dur
tipo , n, dur =tipo_estudio("tec","yeily","6 meses lectivas y 6 meses de practica")
print("su tipo de estudio es:",tipo,"y su nombre es :",n,"y la duracion es de:",dur)

tipo , n , dur =tipo_estudio("tgo","pepito","18 meses lectiva y 6 meses de practica")
print("su tipo de estudio es:",tipo,"y su nombre es :",n,"y la duracion es de:",dur)

tipo , n , dur =tipo_estudio("com","marta","el tiempo en horas 40- horas, 60- horas y 120- horas")
print("su tipo de estudio es:",tipo,"y su nombre es :",n,"y la duracion es de:",dur)	