# Interfaces graficas tambien denominadas GUI, las librerias con las que trabajar para crear GUI son las
# siguientes TKinter, WxPython, PyQT, PyGTK

# Con esta simple instruccion creamos nuestra primera pantalla en python
from tkinter import *

raiz = Tk()

# Darle un titulo a nuestra pantalla
raiz.title('Ventana de Prueba')

# Redimencionar nuestra pantalla
raiz.resizable(1, 0)

# Cambiar el icono de nuestro programa
raiz.iconbitmap('Mana logo.ico')

# Cambiar el tamano de nuestra pantalla
raiz.geometry('650x350')

# Cambiar el color de fondo de nuestra pantalla
raiz.config(bg='blue')

raiz.mainloop()
