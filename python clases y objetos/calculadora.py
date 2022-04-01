""" Cree una clase calculadora básica (suma, resta, multiplicación y división) en la clase
calculadora.py.
"""
class calculadora():
	total=0
	def __init__(self, a1,a2):
		self.a1 = (a1)
		self.a2=(a2)
		calculadora.total+=1
	def mostrarTotal(self):
		print("total %d",calculadora.total)
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
		

a1=5
a2=12
calculadora=calculadora(a1,a2)
calculadora.suma()
calculadora.resta()
calculadora.mult()
calculadora.div()
calculadora.mostrarTotal()

del calculadora
calculadora.get()

