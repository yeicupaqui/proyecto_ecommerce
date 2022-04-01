nombre=input("ingrese su nombre:")
taller=float(input("ingrese la nota de taller:"))
quiz=float(input("ingrese la nota de quiz:"))
parcial=float(input("ingrese la nota de parcial:"))

pt=taller*20/100
pq=quiz*30/100
pp=parcial*50/100
tn=pt+pq+pp

print (pt)
print (pq)
print (pp)

if tn >= 3.5:
	print("el estudiante ", nombre ," aprobo y nota es :",tn)
else:
	print("el estudainte ", nombre ," no aprobo su nota es :", tn)

