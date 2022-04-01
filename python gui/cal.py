from tkinter import *
import tkinter 

ventana=Frame(height=250,width=450)
ventana.pack(padx=5,pady=5)

def sumar():
	resultado=int(numero1.get())+int(numero2.get())
	Label(text=resultado,font=("Broadway",15),fg="blue").place(width=50,x=200,y=160)


def resta():
	resultado=int(numero1.get())-int(numero2.get())
	Label(text=resultado,font=("Broadway",15),fg="blue").place(width=50,x=200,y=160)


def multiplicacion():
	resultado=int(numero1.get())*int(numero2.get())
	Label(text=resultado,font=("Broadway",15),fg="blue").place(width=50,x=200,y=160)


def divicion():
	resultado=int(numero1.get())/int(numero2.get())
	Label(text=resultado,font=("Broadway",15),fg="blue").place(width=50,x=200,y=160)

resultado=0
numero1=IntVar()
numero2=IntVar()
titulo=Label(text="operaciones basicas ",font=("Algerian",15)).place(x=150,y=30)
n1=Entry(textvariable=numero1).place(width=130,x=180,y=60)
n2=Entry(textvariable=numero2).place(width=130,x=180,y=90)
bsumar=Button(text="suma",command=sumar).place(width=80,x=50,y=120)
botonre=Button(text="resta",command=resta).place(width=80,x=150,y=120)
botonpor=Button(text="multiplicacion",command=multiplicacion).place(width=90,x=250,y=120)
botondi=Button(text="divicion",command=divicion).place(width=80,x=350,y=120)
ventana.mainloop()