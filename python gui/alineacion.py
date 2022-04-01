from tkinter import*
ventana=Tk()
ventana.geometry("433x700+100+68")
ventana.config(bg="whitesmoke")
ventana.title("seleccion colombia")

Imagenfondo=PhotoImage(file="imagenes/fondo.png")
Fondo=Label(ventana, image=Imagenfondo).place(x=0,y=0)

Falca=PhotoImage(file="imagenes/j01.png")
jug1=Label(ventana, image=Falca).place(x=170,y=70)

Quinte=PhotoImage(file="imagenes/j1.png")
jug2=Label(ventana, image=Quinte).place(x=40,y=170)

James=PhotoImage(file="imagenes/j3.png")
jug3=Label(ventana, image=James).place(x=170,y=170)

Cuadrado=PhotoImage(file="imagenes/j4.png")
jug4=Label(ventana, image=Cuadrado).place(x=310,y=170)

Barrios=PhotoImage(file="imagenes/j5.png")
jug5=Label(ventana, image=Barrios).place(x=100, y=280)

Sanchez=PhotoImage(file="imagenes/j6.png")
jug6=Label(ventana, image=Sanchez).place(x=250, y=280)

Diaz=PhotoImage(file="imagenes/j7.png")
jug7=Label(ventana, image=Diaz).place(x=18, y=400)

DSanchez=PhotoImage(file="imagenes/j8.png")
jug8=Label(ventana, image=DSanchez).place(x=100, y=500)

Mina=PhotoImage(file="imagenes/j10.png")
jug9=Label(ventana, image=Mina).place(x=228, y=500)

Arias=PhotoImage(file="imagenes/j11.png")
jug10=Label(ventana, image=Arias).place(x=316, y=400)

Ospina=PhotoImage(file="imagenes/j2.png")
jug11=Label(ventana, image=Ospina).place(x=170,y=600)

ventana.mainloop()
