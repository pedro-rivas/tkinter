from tkinter import *
#config
root = Tk()
root.title("Calculadora de IMC")

# frame = Frame(root)
# frame.pack()
# frame.config(width=480,height=300)

#variales
weight = StringVar()
height = StringVar()
age = StringVar()
imc = StringVar()

#labels
Label(root, text="¿Cúal es tu peso? (kg)").grid(row=0, column=0)
Entry(root, textvariable=weight).grid(row=0, column=1, padx=5, pady=5)

Label(root, text="¿Cúal es tu estatura? (cm)").grid(row=1, column=0)
Entry(root, textvariable=height).grid(row=1, column=1, padx=5, pady=5)

Label(root, text="¿Cúal es tu edad? (años)").grid(row=2, column=0)
Entry(root, textvariable=age).grid(row=2, column=1, padx=5, pady=5)



#functions
def showImc():
    calculateImc()
    Label(root, text="Tu imc es: ").grid(row=3, column=0, padx=5, pady=5)
    Entry(root, textvariable=imc, state="disable").grid(row=3, column=1, padx=5, pady=5)

def calculateImc():
    _weight = float(weight.get())
    _height = float(height.get())/100
    _imc = _weight/(_height * _height)
    imc.set(_imc)

#button
Button(root, text="Cácular IMC", command=showImc).grid(row=4, column=1, padx=5, pady=5)


#loop
root.mainloop()