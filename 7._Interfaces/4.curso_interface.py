# Widget Entry
# La propiedad sticky podemos ubicafr elemntos de nuestra interfaz usando los puntos cardinales

from tkinter import *

root = Tk()

miFrame = Frame(root, width=1200, height=600)
miFrame.pack()

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg='red', justify='center')

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1)
cuadroPass.config(show='*')

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1)

nombreLabel = Label(miFrame, text='Nombre:')
nombreLabel.grid(row=0, column=0, sticky='e', pady=10, padx=10)

passLabel = Label(miFrame, text='Password:')
passLabel.grid(row=1, column=0, sticky='e', pady=10, padx=10)


apellidoLabel = Label(miFrame, text='Apellido:')
apellidoLabel.grid(row=2, column=0, sticky='e', pady=10, padx=10)

direccionLabel = Label(miFrame, text='Direccion:')
direccionLabel.grid(row=3, column=0, sticky='e', pady=10, padx=10)

root.mainloop()
