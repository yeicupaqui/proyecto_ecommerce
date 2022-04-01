class punto():
	def __init__(self, x=0,y=0):
		self.x = x
		self.y=y

	def __del__(self):
		nombre_clase="punto"
		print(nombre_clase,"Destroyed")

pt1=punto()
pt2=pt1
pt3=pt1
print(id(pt2),id(pt2),id(pt3))


del pt1
del pt2
del pt3
"""
#1tarea definir que es una excepcion en pythn
#2tarea crear un ejercicio donde ejecute una excepcion
dar ejemplo como se maneja