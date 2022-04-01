"""
crear una funcion que reciba el dato de tipo 
de estudio y retorne en que tipo se encuentra estudiando
en el sena ejemplo: 
tipo:
tec=tecnico
teg=tegnologo
com=complememtario
"""
def tipo_estudio(tipo):
	if tipo=="tec":
		return"tecnico"
	elif tipo=="teg":
		return"tegnologo"
	else:
		return"complementario"

print(tipo_estudio("tec"),"el tipo de estudio de yeily")
print(tipo_estudio("teg"),"el tipo de estudio de pepito")
print(tipo_estudio("com"),"el tipo de estudio de marta")
