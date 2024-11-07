# Los frames: una estructura de ventana con TK siempre debe contener uno o mas Frame
# en el frame es donde vas los widgets

from tkinter import *

raiz = Tk()

raiz.title('Frames')

# raiz.geometry('650x350')

raiz.config(bg='blue')

# Construir nuestro Frame
miFrame = Frame()

# Empaquetar el frame
# miFrame.pack(side='bottom', anchor='n')
miFrame.pack(fill='both', expand=True)

# Cambiar las caracteristcias del borde del frame

miFrame.config(bd=35)
miFrame.config(relief='sunken')

# Darle color a nuestro Frame
miFrame.config(bg='red')

# Darle tamagno a nestro frame: un frame tiene un tamagno fijo
miFrame.config(width='650', height='350')

# Cambiar el cursor del raton
miFrame.config(cursor='hand2')

raiz.mainloop()
