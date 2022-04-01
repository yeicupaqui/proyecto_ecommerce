class Padre1:
	def myMethod(self):
		print("llamar el metodo Padre1")

class Hijo1(Padre1):
	def myMethod(self):
		print("llamar el metodo Hijo1")

c=Hijo1()
c.myMethod()
p=Padre1()
p.myMethod()