from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import subprocess

root = Tk()
root.title("Pizzerola")
root.iconbitmap("pizza.ico")

myFont = font.Font(family='Noteworthy', size=20)

texto=StringVar()
texto.set("No hay otras iguales")

texto1=StringVar()
texto1.set("Pizzerola")

frame=Frame(root, width=200, height=120)
frame.pack()


Label(frame, text="").pack()
label=Label(frame, text="Las mejores")
label.pack()
label.config(font=("olivier", 42))
label.config(textvariable=texto1)

imagen=PhotoImage(file="pizza.gif")
Label(frame, text="").pack()
Label(frame,image=imagen, bd=0).pack()

label=Label(frame, text="La mejor")
label.pack()
label.config(font=("olivier", 32))
label.config(textvariable=texto)

Label(frame, text="").pack()
Label(frame, text="").pack()
label=Label(frame, text="Elige tu pizzerola")
label.pack()
label.config(font=("Cream Peach", 28))

frame1=Frame(root, width=200, height=120)


pixelVirtual = PhotoImage(width=2, height=2)

def seleccionar(ventana,queso,peperoni):
	cadena = ""
	if (queso.get()):
		cadena += "Con queso extra"
	else:
		cadena += "Sin queso extra"

	if (peperoni.get()):
	    cadena += " y con peperoni"
	else:
	    cadena += " y sin peperoni"

	
	ventana.monitor.config(text=cadena)   	


def reset(ventana,queso,peperoni):
	queso.set(0)
	peperoni.set(0)
	ventana.monitor.config(text="Sin queso extra y sin peperoni")	

def pedido():
	messagebox.showinfo("Tu pedido","DELIIIII, Pizza en preparacion!!")





def message(mensaje):
	ventana = Toplevel(root)
	ventana.title(mensaje)
	ventana.config(bd=15)
	image=PhotoImage(file="Gigante.gif")
	Label(ventana, image=image).pack(side="left")
	
	frame2=Frame(ventana)
	frame2.pack()

	queso=IntVar()
	peperoni=IntVar()

	Label(frame2, text="Como quieres la pizza?").pack(anchor="w")
	Checkbutton(frame2, text="Con queso extra", variable=queso, onvalue=1, offvalue=0, command=lambda: seleccionar(ventana,queso,peperoni)).pack(anchor="w")
	Checkbutton(frame2, text="Con peperoni", variable=peperoni,command=lambda:seleccionar(ventana,queso,peperoni)).pack(anchor="w")
	ventana.monitor = Label(frame2,text="Sin queso extra y sin peperoni")
	ventana.monitor.pack()

	Button(frame2, text="Comienza de nuevo", command=lambda: reset(ventana,queso,peperoni)).pack()
	Button(frame2, text="Hacer tu pedido", command=pedido).pack()
	ventana.mainloop() 


button1 = Button(frame1, text="Delgarola", image=pixelVirtual, width=70, height=50, compound="c", command=lambda: message("Delgarola"))
button1['font'] = myFont
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = Button(frame1, text="Cacerola", image=pixelVirtual, width=70, height=50, compound="c", command=lambda: message("Cacerola"))
button2['font'] = myFont
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = Button(frame1, text="Chicanola", image=pixelVirtual, width=70, height=50, compound="c", command=lambda: message("Chicanola"))
button3['font'] = myFont
button3.grid(row=1, column=0, padx=10, pady=10)

button4 = Button(frame1, text="No Gluten", image=pixelVirtual, width=70, height=50, compound="c", command=lambda: message("No Gluten"))
button4['font'] = myFont
button4.grid(row=1, column=1, padx=10, pady=10)

frame1.pack()


root.mainloop()


