for i in range(10):
	print(i)

def imprimir_texto( str ):
	"imprime el texto que llega como parametro"
	print(str)
	return
imprimir_texto("hola mundo")

def changlist( mylist):
	"cambia una lista con nuevos valores"
	mylist.append([1,2,3,4]);
	print("valores dentro de la funcion:",mylist)
	return
mylist=[10,20,30];
changlist( mylist );
print("valores fuera de la funcion:",mylist)

def printinfo(name,age):
	"imprime variables de esta funcion"
	print("name:",name)
	print("age",age)
	return;
printinfo(age=10,name="yeily")


def printinfo(name,edad=100):
	"imprime variables de esta funcion"
	print("name:",name)
	print("edad:",edad)
	return;
printinfo( name="yeily")


def printifo(arg1,*varios):
	"imprimir parametros enviados y usar argumentos de longitud variable"
	print("resultado es : ")
	print(arg1)
	for var in varios:
		print("var:",var)
	return;
printifo(10)
printifo(70,60,90)

nombre="nombre por defecto"
def nombre_completo(name="yeily",apellido="cupaqui"):
	"retorne nombre completo"
	nombre=name+" "+apellido
	print("local variable",nombre)
	return nombre;

nombre_completo(name="laura",apellido="cruz")
print("global",nombre)