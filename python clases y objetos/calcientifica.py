import math
class calcientifica():
	total=0
	def __init__(self, a1,a2):
		self.a1 =(a1)
		self.a2=(a2)
		calcientifica.total+=1
	def mostrarTotal(self):
		print("total %d",calcientifica.total)
	def potencia(self):
		potencia=self.a1**a2
		print("el resultado de la potencia es:",potencia)
	def raiz(self):
		raiz=math.sqrt(a1) 
		print("el resultado de la raiz es:",raiz)
	def suma(self):
		suma=self.a1 + self.a2
		print("el resultado de la suma es:",suma)
	def resta(self):
		resta=self.a1 - self.a2
		print("el resultado de la resta es:",resta)
	def mult(self):
		mult=self.a1 * self.a2
		print("el resultado de la multiplicacion es:",mult)
	def div(self):
		div=self.a1 / self.a2
		print("el resultado de la divicion es:",div)
	def __del__(self):
		pass

a1=6
a2=12
calcientifica=calcientifica(a1,a2)
calcientifica.potencia()
calcientifica.raiz()
calcientifica.suma()
calcientifica.resta()
calcientifica.mult()
calcientifica.div()
calcientifica.mostrarTotal()

del calcientifica
calcientifica.get()