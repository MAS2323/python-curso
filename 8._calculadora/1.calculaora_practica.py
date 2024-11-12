
from tkinter import *

# Creacion de la raiz de nuestra interfaz grafica
raiz = Tk()

# Creacion de nuestro Frame principal
miFrame = Frame(raiz)
miFrame.pack()

# Variable global
operacion = ""


# --------------------------Pantalla--------------------------------------
# Esta interface se construira con un Entry
# Usaremos el metodo grid para poder confeccionar filas y columnas

numeroPantalla = StringVar()


pantalla = Entry(miFrame, textvariable=numeroPantalla)
# Para que la pantalla ocupe mas de una columna usamos la siguiente funcion columnspan=4
# en este ejemplo ocuparemos 4 columnas
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="#000", fg="#03f943", justify='right')

# --------------------Pulsaciones del teclado (Funciones)---------------------


def numeroPulsado(numero):

    global operacion

    if operacion != "":
        numeroPantalla.set(numero)

        operacion = ""
    else:

        numeroPantalla.set(numeroPantalla.get() + numero)


# -------------------Funcion Suma------------------------------------
def suma():

    global operacion

    operacion = "suma"


# -----------------------Primera fila de botones----------------------------

# ---------------Fila uno(1)---------------------------------

botton7 = Button(miFrame, text="7", width=3,
                 command=lambda: numeroPulsado("7"))
botton7.grid(row=2, column=1)
botton8 = Button(miFrame, text="8", width=3,
                 command=lambda: numeroPulsado("8"))
botton8.grid(row=2, column=2)
botton9 = Button(miFrame, text="9", width=3,
                 command=lambda: numeroPulsado("9"))
botton9.grid(row=2, column=3)
bottonDiv = Button(miFrame, text="/", width=3)
bottonDiv.grid(row=2, column=4)


# ---------------Fila Dos(2)---------------------------------

botton4 = Button(miFrame, text="4", width=3,
                 command=lambda: numeroPulsado("4"))
botton4.grid(row=3, column=1)
botton5 = Button(miFrame, text="5", width=3,
                 command=lambda: numeroPulsado("5"))
botton5.grid(row=3, column=2)
botton6 = Button(miFrame, text="6", width=3,
                 command=lambda: numeroPulsado("6"))
botton6.grid(row=3, column=3)
bottonMult = Button(miFrame, text="x", width=3)
bottonMult.grid(row=3, column=4)


# ---------------Fila Tres(3)---------------------------------

botton1 = Button(miFrame, text="1", width=3,
                 command=lambda: numeroPulsado("1"))
botton1.grid(row=4, column=1)
botton2 = Button(miFrame, text="2", width=3,
                 command=lambda: numeroPulsado("2"))
botton2.grid(row=4, column=2)
botton3 = Button(miFrame, text="3", width=3,
                 command=lambda: numeroPulsado("3"))
botton3.grid(row=4, column=3)
bottonRest = Button(miFrame, text="-", width=3)
bottonRest.grid(row=4, column=4)


# ---------------Fila Cuatro(4)---------------------------------

botton0 = Button(miFrame, text="0", width=3,
                 command=lambda: numeroPulsado("0"))
botton0.grid(row=5, column=1)
bottonComa = Button(miFrame, text=",", width=3,
                    command=lambda: numeroPulsado(","))
bottonComa.grid(row=5, column=2)
bottonIgual = Button(miFrame, text="=", width=3)
bottonIgual.grid(row=5, column=3)
bottonSuma = Button(miFrame, text="+", width=3, command=lambda: suma())
bottonSuma.grid(row=5, column=4)

# ------------------Tecla para eliminar valores-----------------------
bottonEliminar = Button(miFrame, text="c", width=3, justify='left',
                        command=lambda: numeroPulsado(","))
bottonEliminar.grid(row=6, column=4)


raiz.mainloop()
