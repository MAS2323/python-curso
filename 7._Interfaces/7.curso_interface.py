from tkinter import *

root = Tk()
root.title('Ejemplo')

# Creacion de las variables para darle funcionalidad a nuestros checkbutton

playa = IntVar()
monte = IntVar()
turismoRural = IntVar()

# ---------Creacion de las funciones-----------


def opcionesViaje():

    opcionEscogida = ""

    if (playa.get() == 1):
        opcionEscogida += "playa"

    if (monte.get() == 1):
        opcionEscogida += 'monte'

    if (turismoRural.get() == 1):

        opcionEscogida += 'Turismo rural'

    textoFinal.config(text=opcionEscogida)

# foto = PhotoImage(file="avion.png")
# Label(root, image=foto).pack()


frame = Frame(root)
frame.pack()

Label(frame, text='Elige destinos', width=50).pack()

# La funcion onvalue='' sirve para determinar el valor que tendra nuestro boton si es seleccionado
# mientras que el offvalue = hace lo contrario

Checkbutton(root, text='playa', variable=playa, onvalue=1,
            offvalue=0, command=opcionesViaje).pack()

Checkbutton(root, text='Montaña', variable=monte, onvalue=1,
            offvalue=0, command=opcionesViaje).pack()

Checkbutton(root, text='Turismo rural', variable=turismoRural,
            onvalue=1, offvalue=0, command=opcionesViaje).pack()


textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()
