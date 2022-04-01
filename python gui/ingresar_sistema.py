from tkinter import*
from tkinter import ttk 
def ingresar(*args):
	try:
		usu=user.get()
		pas=passw.get()
		if(usu=="ADMIN" and pas=="ADMIN"):
			print("usuario valido")
		else:
			print("usuario no valido")
		#resultado.set(s)
	except ValueError:
		pass
root=Tk()
root.title("sistema centro odontologico")
mainframe = ttk.Frame(root, padding = "3 3 12 12 ")
mainframe.grid(column=0, row=0, stick=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
user = StringVar()
passw= StringVar()
resultado= StringVar()
feet_entry = ttk.Entry(mainframe, width=7 , textvariable=user)
feet_entry.grid(column=2 ,row=1, stick=(W,E))
feet_entry2 = ttk.Entry(mainframe, width=7 , textvariable=passw)
feet_entry2.grid(column=2 ,row=2, stick=(W,E))
ttk.Button(mainframe, text="ingresar", command=ingresar).grid(column=3, row=4 , stick=(W))
ttk.Label(mainframe, text="usuario").grid(column=1 , row=1, stick=E)
ttk.Label(mainframe, text="contraseña ").grid(column=1 , row=2, stick=E)
feet_entry.focus()
root.mainloop()
