# Ventanas emergentes: Abrir archivos

from tkinter import *
from tkinter import filedialog


root = Tk()


def abreFichero():

    # Para determinar el directorio donde queremos que se abra nuestra ventana usamos el siguiente metodo initialdir='lugar'
    # Para determinar el tipo de archivo que queremos ver usamos el metodo filetypes=(())
    fichero = filedialog.askopenfilename(
        title='Abrir', initialdir='C:', filetypes=(('Ficheros de excel', '*.xlsx'),
                                                   ("Ficheros de text", "*.txt"), ('Todos los ficheros', "*.*")))
    print(fichero)


boton = Button(root, text='Abrir fichero', command=abreFichero)
boton.pack()

root.mainloop()
