from tkinter import *
from tkinter import ttk 
def calculate(*args):
	try:
		value = float(feet.get())
		meters.set(0.3049* value * 10000.0 + 0.500/10000)
	except ValueError:
		pass
root =Tk()
root.title("feet to meters")
mainframe = ttk.Frame(root, padding = "3 3 12 12 ")
mainframe.grid(column=0, row=0, stick=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
feet = StringVar()
meters= StringVar()
feet_entry = ttk.Entry(mainframe, width=7 , textvariable=feet)
feet_entry.grid(column=2 ,row=1, stick=(W,E))
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2  , stick=(W,E))
ttk.Button(mainframe, text="calculate", command=calculate).grid(column=3, row=3 , stick=(N))
ttk.Label(mainframe, text="feet").grid(column=3 , row=1, stick=(W))
ttk.Label(mainframe, text="is equivalent to ").grid(column=1 , row=2, stick=(E))
ttk.Label(mainframe, text="meters").grid(column=3 , row=2, stick=(W))
for child in mainframe.winfo_children():child.grid_configure(padx=5 , pady=5)
feet_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()
