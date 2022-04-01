class Aprendiz():
	"clase Aprendices sena"
	total=0
	def __init__(self, name,lastname):
		self.nombre = name
		self.apellido=lastname
		Aprendiz.total+=1

	def mostrarTotal(self):
		print("total %d",Aprendiz.total)

	def mostrarAprendiz(self):
		print("nombre:",self.nombre,"apellido:",self.apellido)
		