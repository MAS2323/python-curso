# Los RadioButton

from tkinter import *

root = Tk()

varOption = IntVar()


def imprimir():
    # Utilisando el get podemos rescatar el valor que el usuario elige al presionar el Radiobutton
    # print(varOption.get())

    if varOption.get() == 1:

        etiqueta.config(text='Has elegido masculino')
    else:

        etiqueta.config(text='Has elegido femenino')


Label(root, text='Genero:').pack()
# Asi es como se crean los Radiobutton

Radiobutton(root, text='Masculino', variable=varOption,
            value=1, command=imprimir).pack()
Radiobutton(root, text='Femenino', variable=varOption,
            value=2, command=imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()


root.mainloop()
