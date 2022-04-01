class Padre:
	parentAttr=100
	def __init__(self):
		print("constructor de la clase padre")

	def parentMethod(self):
		print("llamado metodo de padre")
	def setAttr(self,attr):
		Padre.parentAttr=attr
	def getAttr(self):
		print("el atributo padre:",Padre.parentAttr)

class Hija(Padre):
	def __init__(self):
		print("constructor de la clase hija")

	def childMethod(self):
		print("llamado el metodo des la clase hija")

c=Hija()
c.childMethod()
c.parentMethod()
c.setAttr(500)
c.getAttr()