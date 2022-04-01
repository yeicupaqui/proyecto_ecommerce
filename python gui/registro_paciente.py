from tkinter import*
from tkinter import ttk 
def registrar(*args):
	try:
	    nom=nombre.get()
	    ape=apellido.get()
	    di=direccion.get()
	    te=telefono.get()
	    cor=correo.get()
	    est=estrato.get()
	    tip=tsangre.get()
	    gen=genero.get()
	    acu=acudiente.get()

	    if(registrar):
	    	print("registro valido")
	    else:
	    	print("cancelar registro")
		
	except ValueError:
		pass
root=Tk()
root.geometry("300x350")
root.title("REGISTRAR PACIENTE")
mainframe = ttk.Frame(root, padding = "48 40 24 12 ")
mainframe.grid(column=0, row=0, stick=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
nombre = StringVar()
apellido= StringVar()
direccion= StringVar()
telefono= StringVar()
correo= StringVar()
estrato= StringVar()
tsangre = StringVar()
genero= StringVar()
acudiente= StringVar()
feet_entry = ttk.Entry(mainframe, width=7 , textvariable=nombre)
feet_entry.grid(column=2 ,row=1, stick=(W,E))
feet_entry2 = ttk.Entry(mainframe, width=7 , textvariable=apellido)
feet_entry2.grid(column=2 ,row=2, stick=(W,E))
feet_entry = ttk.Entry(mainframe, width=7 , textvariable=direccion)
feet_entry.grid(column=2 ,row=3, stick=(W,E))
feet_entry2 = ttk.Entry(mainframe, width=7 , textvariable=telefono)
feet_entry2.grid(column=2 ,row=4, stick=(W,E))
feet_entry = ttk.Entry(mainframe, width=7 , textvariable=correo)
feet_entry.grid(column=2 ,row=5, stick=(W,E))
feet_entry2 = ttk.Entry(mainframe, width=7 , textvariable=estrato)
feet_entry2.grid(column=2 ,row=6, stick=(W,E))
feet_entry = ttk.Entry(mainframe, width=7 , textvariable=tsangre)
feet_entry.grid(column=2 ,row=7, stick=(W,E))
feet_entry2 = ttk.Entry(mainframe, width=7 , textvariable=genero)
feet_entry2.grid(column=2 ,row=8, stick=(W,E))
feet_entry = ttk.Entry(mainframe, width=7 , textvariable=acudiente)
feet_entry.grid(column=2 ,row=9, stick=(W,E))
ttk.Button(mainframe, text="registrar", command=registrar).grid(column=1, row=10 , stick=(W))
ttk.Button(mainframe, text="cancelar", command=registrar).grid(column=2, row=10 , stick=(W))
ttk.Label(mainframe, text="nombres ").grid(column=1 , row=1, stick=E)
ttk.Label(mainframe, text="apellidos").grid(column=1 , row=2, stick=E)
ttk.Label(mainframe, text="direccion").grid(column=1 , row=3, stick=E)
ttk.Label(mainframe, text="telefono").grid(column=1 , row=4, stick=E)
ttk.Label(mainframe, text="correo").grid(column=1 , row=5, stick=E)
ttk.Label(mainframe, text="estrato").grid(column=1 , row=6, stick=E)
ttk.Label(mainframe, text="tipo sangre").grid(column=1 , row=7, stick=E)
ttk.Label(mainframe, text="genero").grid(column=1 , row=8, stick=E)
ttk.Label(mainframe, text="acudiente").grid(column=1 , row=9, stick=E)
feet_entry.focus()
root.mainloop()