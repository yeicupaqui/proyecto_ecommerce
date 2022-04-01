pago=int(input("digite el pago:"))
print(pago)

if pago >=20000:
	print("puede accedes al servicio su excedente es de : ", pago-20000)
else:
	print("no puede aceder al servicio y debe : ", 20000-pago)