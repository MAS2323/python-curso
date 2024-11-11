from tkinter import *

# Widgets text y Button

# Widgets text: sirve para introducir texto largo en nuestra interfaz grafica
# Widgets Button sirve para interactuar con la interfaz, etc

"""
Cuando uzamos los widgets tenemos primero que decir al widget en cuestion quien sera el contenedor padre 
en nuestro ejemplo el contenedor padre sera: root, o raiz 

"""

root = Tk()

miFrame = Frame(root, width=1200, height=600)
miFrame.pack()  # Haciendo el pack a nuestra raiz

# StringVar hace referencia a una cadena de caracteres
miNombre = StringVar()

# con textvariable asociamos la variable creada con el cuadro
cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg='red', justify='center')

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1)
cuadroPass.config(show='*')

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, pady=10, padx=10)

# Para usar el scroll en nuestra app de python lo tenemos que construir
# Asi es como contruimos un escroll vertical para el campo textoComentario
scrollVer = Scrollbar(miFrame, command=textoComentario.yview)
scrollVer.grid(row=4, column=2, sticky=NSEW)

textoComentario.config(yscrollcommand=scrollVer.set)

nombreLabel = Label(miFrame, text='Nombre:')
nombreLabel.grid(row=0, column=0, sticky='e', pady=10, padx=10)

passLabel = Label(miFrame, text='Password:')
passLabel.grid(row=1, column=0, sticky='e', pady=10, padx=10)


apellidoLabel = Label(miFrame, text='Apellido:')
apellidoLabel.grid(row=2, column=0, sticky='e', pady=10, padx=10)

direccionLabel = Label(miFrame, text='Direccion:')
direccionLabel.grid(row=3, column=0, sticky='e', pady=10, padx=10)

comentariosLabel = Label(miFrame, text='Comentarios:')
comentariosLabel.grid(row=4, column=0, sticky='e', pady=10, padx=10)


def codigoBoton():
    # Cuando pulsamos el boton asignamos el vaor de nuestra variable
    miNombre.set("Juan")

# Para obtener la informacion de un cuadro de texto utilizamos la funcion get


# Si cambiamos la raiz de nuestro boton tambien cambiara su posicion
botonEnvio = Button(root, text="Eviar", command=codigoBoton)
botonEnvio.pack()


root.mainloop()
