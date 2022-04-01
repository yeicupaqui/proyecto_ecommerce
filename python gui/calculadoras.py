from tkinter import *
ventana = Frame(height=250 , width=350, bg="skyblue2")
ventana.pack(padx=5, pady=5)
calculo=" "
resultado=0
titulo = Label(text="Calculadora Basica", font=("Alegrian", 15), fg="blue2").place(x=65, y=20)
digito = StringVar()
entrada_digito = Entry(textvariable=digito, font=("Alegrian", 15),fg="white", bg="blue4").place(width=160,x=100,y=60)
boton1 = Button(text="1", command=lambda:mostrar_numero("1")).place(width=50 , x=50, y=90)
boton2 = Button(text="2", command=lambda:mostrar_numero("2")).place(width=50 , x=120, y=90)
boton3 = Button(text="3", command=lambda:mostrar_numero("3")).place(width=50 , x=190, y=90)
boton4 = Button(text="4", command=lambda:mostrar_numero("4")).place(width=50 , x=50, y=130)
boton5 = Button(text="5", command=lambda:mostrar_numero("5")).place(width=50 , x=120, y=130)
boton6 = Button(text="6", command=lambda:mostrar_numero("6")).place(width=50 , x=190, y=130)
boton7 = Button(text="7", command=lambda:mostrar_numero("7")).place(width=50 , x=50, y=170)
boton8 = Button(text="8", command=lambda:mostrar_numero("8")).place(width=50 , x=120, y=170)
boton9 = Button(text="9", command=lambda:mostrar_numero("9")).place(width=50 , x=190, y=170)
boton0 = Button(text="0", command=lambda:mostrar_numero("0")).place(width=50 , x=50, y=210)
botonigual = Button(text=" = ", command=lambda:total()).place(width=50 , x=120, y=210)

botonsu = Button(text=" + " , command=lambda:suma(digito.get())).place(width=50 , x=260 , y=90 )
botonre = Button(text=" - ", command=lambda:resta(digito.get())).place(width=50 , x=260 , y=130)
botonpor = Button(text=" * ", command=lambda:multiplicar(digito.get())).place(width=50 , x=260, y=210)
botondi = Button(text=" / ", command=lambda:dividir(digito.get())).place(width=50 , x=260, y=170)

botonlim= Button(text="c", command=lambda:limpiar()).place(width=50 , x=190, y=210)

def mostrar_numero(numero):
	global calculo
	if calculo !=" ":
		digito.set(numero)
		calculo=" "
	else:
		digito.set(digito.get()+numero)

def suma(numero):
	global calculo
	global resultado
	resultado+=int(numero)
	calculo="suma"
	digito.set(resultado)

def resta(numero):
	global calculo
	global resultado
	resultado-=int(numero)
	calculo="resta"
	digito.set(resultado)

def multiplicar(numero):
	global calculo
	global resultado
	resultado*=int(numero)
	calculo="multiplicar"
	digito.set(resultado)


def dividir(numero):
	global calculo
	global resultado
	resultado/=int(numero)
	calculo="dividir"
	digito.set(resultado)


def total():
	global resultado
	digito.set(resultado+int(digito.get()))

def limpiar():
	digito.set(" ")

ventana.mainloop()

