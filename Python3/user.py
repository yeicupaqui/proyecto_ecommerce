"""
Cree un módulo user.py con una función login que reciba user y password y verifique 
si el user es “admin” y pasword “1234”, retorne un string que diga “login correcto” 
o de otra forma retorne “login incorrecto”
"""
def login(user,password):
	if user=="admin" and password==1234:
		print("login correcto")
	else:
		print ("login incorrecto:")
		return 

def listar(iduser,fecha):
	lista=[]
	lista.append(iduser)
	lista.append(fecha)
	print(lista[:])
	return

def leer_registro(linea1,linea2):
	print("los nombres de archivo de texto son",linea1,linea2)
	return