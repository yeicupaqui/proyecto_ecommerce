from tkinter import *
from tkinter import ttk

root = Tk()

principal = Frame(root)
principal.configure(bg='BLUE')
principal.pack(expand=True, fill='both')


principal.columnconfigure(0, weight=10) # extremo izquierdo

principal.columnconfigure(1, weight=1)

principal.columnconfigure(2, weight=1)

principal.columnconfigure(3, weight=8) # extremo derecho

#------------------------------  FILA 0  ------------------------------

registrar = Label(principal, text="-------REGISTRAR PACIENTE------")
registrar.configure(font=('Verdana', 15, 'bold'))
registrar.grid(row=0, column=2, sticky="w") # COLUMN 2

#------------------------------  FILA 1  ------------------------------
iden = Label(principal, text='IDENTIFICACION')
iden.configure(font=('Verdana', 15, 'bold'))
iden.grid(row=1, column=1, sticky="w") # COLUMN 1

entryiden = Entry(principal)
entryiden.configure(font=('Verdana', 15), justify='center')
entryiden.grid(row=1, column=2, sticky="e") # COLUMN 2

#------------------------------  FILA 2  ------------------------------
nombre = Label(principal, text='NOMBRES')
nombre.configure(font=('Verdana', 15, 'bold'))
nombre.grid(row=2, column=1, sticky="w") # COLUMN 1

entrynombre = Entry(principal)
entrynombre.configure(font=('Verdana', 15), justify='center')
entrynombre.grid(row=2, column=2, sticky="E") # COLUMN 2

#------------------------------  FILA 3  ------------------------------
apellido = Label(principal, text='APELLIDOS')
apellido.configure(font=('Verdana', 15, 'bold'))
apellido.grid(row=3, column=1, sticky="w") # COLUMN 1

entryapellido = Entry(principal)
entryapellido.configure(font=('Verdana', 15), justify='center')
entryapellido.grid(row=3, column=2, sticky="E") # COLUMN 2

#------------------------------  FILA 4 ------------------------------
direccion = Label(principal, text='DIRECCION')
direccion.configure(font=('Verdana', 15, 'bold'))
direccion.grid(row=4, column=1, sticky="w") # COLUMN 1

entrydireccion = Entry(principal)
entrydireccion.configure(font=('Verdana', 15), justify='center')
entrydireccion.grid(row=4, column=2, sticky="e") # COLUMN 2

#------------------------------  FILA 5------------------------------
telefono = Label(principal, text='TELEFONO')
telefono.configure(font=('Verdana', 15, 'bold'))
telefono.grid(row=5, column=1, sticky="w") # COLUMN 1	

entrytelefono = Entry(principal)
entrytelefono.configure(font=('Verdana', 15), justify='center')
entrytelefono.grid(row=5, column=2, sticky="E") # COLUMN 2

#------------------------------  FILA 6 ------------------------------
email = Label(principal, text='DIRECCION')
email.configure(font=('Verdana', 15, 'bold'))
email.grid(row=6, column=1, sticky="w") # COLUMN 1

entryemail = Entry(principal)
entryemail.configure(font=('Verdana', 15), justify='center')
entryemail.grid(row=6, column=2, sticky="e") # COLUMN 2

#------------------------------  FILA 7------------------------------
Estrato = Label(principal, text='ESTRATO')
Estrato.configure(font=('Verdana', 15, 'bold'))
Estrato.grid(row=7, column=1, sticky="w") # COLUMN 1

cestrato=ttk.Combobox(principal)
cestrato["values"]=["1","2","3","4"]
cestrato.configure(font=("verdana",15,"bold"),justify="center")
cestrato.grid(row=7,column=2,sticky="E")

#------------------------------  FILA 7------------------------------
tsangre = Label(principal, text='TIPO SANGRE')
tsangre.configure(font=('Verdana', 15, 'bold'))
tsangre.grid(row=8, column=1, sticky="w") # COLUMN 1

cestrato=ttk.Combobox(principal)
cestrato["values"]=["0+","0-","A+","B+","A-","AB+"]
cestrato.configure(font=("verdana",15,"bold"),justify="center")
cestrato.grid(row=8,column=2,sticky="E")

#------------------------------  FILA 8------------------------------
genero = Label(principal, text='GENERO')
genero.configure(font=('Verdana', 15, 'bold'))
genero.grid(row=9, column=1, sticky="w") # COLUMN 1

cestrato=ttk.Combobox(principal)
cestrato["values"]=["F","M","T","I"]
cestrato.configure(font=("verdana",15,"bold"),justify="center")
cestrato.grid(row=9,column=2,sticky="E")

#------------------------------  FILA 6 ------------------------------
acudiente = Label(principal, text='NOMBRE ACUDIENTE')
acudiente.configure(font=('Verdana', 15, 'bold'))
acudiente.grid(row=10, column=1, sticky="w") # COLUMN 1

entryacudiente = Entry(principal)
entryacudiente.configure(font=('Verdana', 15), justify='center')
entryacudiente.grid(row=10, column=2, sticky="e") # COLUMN 2

def registrar(boton):
	if boton == "Registrar":
		print("Registrar")

	else:
		print("Cancelar")





Btnregistrar = Button(principal, text="REGISTRAR", command= lambda: registrar("Registrar"))
Btnregistrar.configure(font=('Verdana',15, 'bold'),justify='center')
Btnregistrar.grid(row=15,column=1, sticky="W")

Btnregistrar = Button(principal,text="CANCELAR", command=lambda: registrar("Cabcelar"))
Btnregistrar.configure(font=('Verdana',15, 'bold'),justify='center')
Btnregistrar.grid(row=15,column=3, sticky="W")

root.geometry('1024x720')
root.mainloop()


