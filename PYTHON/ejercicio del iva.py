producto=int(input("precio del producto:"))
if producto >= 25000:
	piva=(producto*19)/100
	tp=producto*piva
	print("el producto con iva tiene un precio de : ", tp)
else:
	print("producto sin iva", producto)