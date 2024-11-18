from tkinter import *
from funciones_practica import *

root = Tk()

barraMenu = Menu(root)

root.config(menu=barraMenu, width=300, height=300)

# ----------------------Funciones------------------------

# Funcion para salir de nuestra Aplicacion


def salirApp():

    valor = messagebox.askquestion('Salir', 'Deseas salir de la aplicacion?')

    if valor == 'yes':
        root.destroy()

# Funcion para limpiar los campos de nuestra DB


def limpiarCampos():

    miNombre.set('')
    miId.set('')
    miApellido.set('')
    miDireccion.set('')
    miPass.set('')
    mensajeText.delete(1.0, END)

# Funcion para crear un susuario en nuestra DB


def crearUsuario():
    miConexion = sqlite3.connect('Usuarios')

    miCursor = miConexion.cursor()
    datos = miNombre.get(), miPass.get(), miApellido.get(
    ), miDireccion.get(), mensajeText.get('1.0', END)
    """miCursor.execute(
        "INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get() +
        "', '" + miPass.get() +
        "', '" + miApellido.get() +
        "', '" + miDireccion.get() +
        "', '" + mensajeText.get('1.0', END) + "')"
    )"""
    # Creacion de una consulta parametrizada
    miCursor.execute(
        'INSERT INTO DATOSUSUARIOS VALUES(NULL, ?,?,?,?,?)', (datos)
    )
    miConexion.commit()

    messagebox.showinfo('BBDD', 'Registro insertado con exito')


# Funcion para leer los datos de nuestra DB
def leer():
    miConexion = sqlite3.connect('Usuarios')

    miCursor = miConexion.cursor()

    miCursor.execute(
        'SELECT * FROM DATOSUSUARIOS WHERE ID=' + miId.get()
    )
    elUsuario = miCursor.fetchall()
    for usuario in elUsuario:
        # Rescatando todos los valores de nuestros campos
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        mensajeText.insert(1.0, usuario[5])

    miConexion.commit()

# Funcion para actualizar los datos de nuestra DB


def actualizar():
    miConexion = sqlite3.connect('Usuarios')

    miCursor = miConexion.cursor()
    datos = miNombre.get(), miPass.get(), miApellido.get(
    ), miDireccion.get(), mensajeText.get('1.0', END)
    # miCursor.execute(
    #     "UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO = '" + miNombre.get() +
    #     "', PASSWORD='" + miPass.get() +
    #     "', APELLIDO='" + miApellido.get() +
    #     "', DIRECCION='" + miDireccion.get() +
    #     "', COMENTARIOS='" + mensajeText.get('1.0', END) +
    #     "' WHERE ID=" + miId.get()
    # )
    miCursor.execute(
        "UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD =?, APELLIDO=?, DIRECCION=?, COMENTARIOS=?" +
        "WHERE ID=" + miId.get(), (datos)
    )
    miConexion.commit()

    messagebox.showinfo('BBDD', 'Registro actualizado con exito')

# Funcion para borrar Los usuarios de nuestra bases de datos DB


def eliminar():

    miConexion = sqlite3.connect('Usuarios')

    miCursor = miConexion.cursor()

    miCursor.execute(
        'DELETE FROM DATOSUSUARIOS WHERE ID=' + miId.get()
    )

    miConexion.commit()
    messagebox.showinfo('BBDD', 'Registro eliminado con exito')


# Los archivos seran los subcampos que se relacionaran con las barras menu o menuprincipal
archivoMenu = Menu(barraMenu, tearoff=0)
archivoBorrar = Menu(barraMenu, tearoff=0)
archivoCrud = Menu(barraMenu, tearoff=0)
archivoAyuda = Menu(barraMenu, tearoff=0)


# ---------Archivos de subcampo Borrar----------------------
archivoBorrar.add_command(label='Borrar campos', command=limpiarCampos)


# -----------Archivos de menu de Ayuda--------------------------------
archivoAyuda.add_command(label='Licencia')
archivoAyuda.add_command(label='Acerca de...')

# --------Archivos de subcampo DDBB------------------------------------------
archivoMenu.add_command(label='Conectar', command=conexionBBDD)
archivoMenu.add_command(label='Salir', command=salirApp)


# ----------------Sub menu del campo Menu Crud-------------------------------
archivoCrud.add_command(label='Crear', command=crearUsuario)
archivoCrud.add_command(label='Leer', command=leer)
archivoCrud.add_command(label='Actualizar', command=actualizar)
archivoCrud.add_command(label='Eliminar', command=eliminar)


# ----------------La barraMenu se asocia a los archivos de subMenu----------------
barraMenu.add_cascade(label='BBDD', menu=archivoMenu)
barraMenu.add_cascade(label='Borrar', menu=archivoBorrar)
barraMenu.add_cascade(label='CRUD', menu=archivoCrud)
barraMenu.add_cascade(label='Ayuda', menu=archivoAyuda)

# Vamos a crear un frmae para manejar los campos de nuestro formulario

miFrame = Frame(root)
miFrame.pack()
miFrame.config(width=300, height=300)

# Usamos el metodo Entry para hacer los campos de nuestro formulario
# usamos el grid para posicionar nuestros campos

# --------------Aqui van todos nuestros Entrys---------------------

# Para que los label puedan reconocer los textos que introducimos en ellos y enviarlos
# a la base de datos tentemos que usar el metodo StringVar() en nuestros Entrys
miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion = StringVar()

# anadiendo el textvariable= variable decimos que en nuestros Entrys
# abran cadena de caracteres

identificador = Entry(miFrame, textvariable=miId)
identificador.grid(row=0, column=1, padx=10, pady=10)

nombre = Entry(miFrame, textvariable=miNombre)
nombre.grid(row=1, column=1, padx=10, pady=10)


password = Entry(miFrame, textvariable=miPass)
password.grid(row=2, column=1, padx=10, pady=10)
password.config(show='*')

apellido = Entry(miFrame, textvariable=miApellido)
apellido.grid(row=3, column=1, padx=10, pady=10)

direccion = Entry(miFrame, textvariable=miDireccion)
direccion.grid(row=4, column=1, padx=10, pady=10)

mensajeText = Text(miFrame, width=16, height=7)
mensajeText.grid(row=5, column=1, padx=10, pady=10)
scroolVart = Scrollbar(miFrame, command=mensajeText.yview)
scroolVart.grid(row=5, column=2, sticky='nsew')
mensajeText.config(yscrollcommand=scroolVart.set)

# -------------Aqui van todos nuestros Labels (Campos)---------------

identificadorLabel = Label(miFrame, text='Id:')
identificadorLabel.grid(row=0, column=0)

nombreLabel = Label(miFrame, text='Nombre:')
nombreLabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

passwordLabel = Label(miFrame, text='Password:')
passwordLabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

apellidoLabel = Label(miFrame, text='Apellido:')
apellidoLabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)

direccionLabel = Label(miFrame, text='Direccion:')
direccionLabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

mensajeLabel = Label(miFrame, text='Comentarios:')
mensajeLabel.grid(row=5, column=0, sticky='e', padx=10, pady=10)


# -------------Aqui van todos nuestros Buttons--------------------
buttonFrame = Frame(root)
buttonFrame.pack()

# Tambien usamos el grid para posicionar los buttons

createButton = Button(buttonFrame, text='Create', command=crearUsuario)
createButton.grid(row=0, column=0, padx=10, pady=10, sticky='e')
readButton = Button(buttonFrame, text='Read', command=leer)
readButton.grid(row=0, column=1, padx=10, pady=10, sticky='e')
updateButton = Button(buttonFrame, text='Update', command=actualizar)
updateButton.grid(row=0, column=2, padx=10, pady=10, sticky='e')
deletButton = Button(buttonFrame, text='Delete', command=eliminar)
deletButton.grid(row=0, column=3, padx=10, pady=10, sticky='e')

root.mainloop()
