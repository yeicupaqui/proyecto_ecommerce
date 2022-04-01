from tkinter import *
from tkinter import ttk 
def suma(*args):
	try:
		num1 = float(n1.get())
		num2 = float(n2.get())
		s=num1+num2
		resultado.set(s)
	except ValueError:
		pass
root =Tk()
root.title("calculadora")
mainframe = ttk.Frame(root, padding = "3 3 12 12 ")
mainframe.grid(column=0, row=0, stick=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
n1 = StringVar()
n2= StringVar()
resultado= StringVar()
feet_entry = ttk.Entry(mainframe, width=7 , textvariable=n1)
feet_entry.grid(column=2 ,row=1, stick=(W,E))
feet_entry = ttk.Entry(mainframe, width=8 , textvariable=n2)
feet_entry.grid(column=2 ,row=2, stick=(N,W))
ttk.Label(mainframe, textvariable=resultado).grid(column=2, row= 3 , stick=(W,E))
ttk.Button(mainframe, text="sumar", command=suma).grid(column=3, row=3 , stick=(W))
ttk.Label(mainframe, text="numero 1").grid(column=1 , row=1, stick=E)
ttk.Label(mainframe, text="la suma es ").grid(column=1 , row=3, stick=N)
ttk.Label(mainframe, text="numero 2").grid(column=1 , row=2, stick=(W))
for child in mainframe.winfo_children():child.grid_configure(padx=5 , pady=5)
feet_entry.focus()
root.bind('<Return>', suma)
root.mainloop()
