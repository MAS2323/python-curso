# Label nos permiten mostrar textos en nuestra interfaz grafica
from tkinter import *

raiz = Tk()


miFrame = Frame(raiz, width=500, height=400)

miFrame.pack()

# La libreria de tkinter solo trabaja con imagenes de formato git y png
miImagen = PhotoImage(file='money-742052_1920-1-1-1.jpg')

Label(miFrame, text='Mas Onewe', fg='red', font=(
    "Comic Sans MS", 18)).place(x=100, y=200)

raiz.mainloop()
