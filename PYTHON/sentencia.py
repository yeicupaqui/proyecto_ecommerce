edad=int(input("ingrese su edad:"))
pago=True
if edad >= 18:
	if pago ==True:
		print("soy mayor de edada y a pagado su recibo")
	else:
		print("es mayor pero no a pagado su ceunta")
else:
	print("soy menor")