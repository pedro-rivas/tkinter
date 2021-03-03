#!/usr/bin/env python
# coding: utf-8

# ## Ejemplo Calculadora !!!

# In[ ]:


from tkinter import *
from math import *

ventana=Tk()
ventana.title("Calculadora básica")
ventana.geometry("350x500")
ventana.configure(background="BlueViolet")
color_boton=("gray77")


def Clik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador) 
    
def clear():
    global operador
    operador=("")
    input_text.set("0")

def operacion():
    global operador
    try:
        op=str(eval(operador))
    except:
        clear()
        op=("ERROR")
    input_text.set(op)

ancho_boton=7
alto_boton=2
input_text=StringVar()
operador=""
clear()
Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=25,y=180)
Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=100,y=180)
Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=175,y=180)
Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=25,y=240)
Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=100,y=240)
Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=175,y=240)
Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=25,y=300)
Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=100,y=300)
Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=175,y=300)
Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=25,y=360)
Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=250,y=180)
Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=250,y=240)
Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=250,y=300)
Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=250,y=360)
Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=100,y=360)
Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=operacion).place(x=175,y=360)

Salida=Entry(ventana,font=('arial',20),width=15,textvariable=input_text,bd=20,insertwidth=4,bg="ivory",justify="right").place(x=25,y=60)

ventana.mainloop()


# In[ ]:





# In[ ]:




