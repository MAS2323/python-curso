# Vetanas emergentes
from tkinter import *
# vamos a importar una libreria que se encarga que crear ventanas emergentes
from tkinter import messagebox
root = Tk()


def infoAdicional():

    # Este metodo consta de dos parametros, el primer parametro
    # consiste en el texto de la barra del titulo y el segundo parametro consiste en texto del cuerpo
    messagebox.showinfo("Procesador de Mas",
                        "Procesador de texto version 2.0.7")

# Tambien se puede modificar el diseno de la ventana emergente
# Vamos a crear la funcion que construira la ventana emergente


def avisoLicencia():

    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")


def salirAplicacion():
    # Este metodo a diferencia del los otros devuelve un valor
    # valor = messagebox.askquestion("Salir", "Desear salir de la aplicaion?")
    valor = messagebox.askokcancel("Salir", "Desear salir de la aplicaion?")

    if valor == True:
        root.destroy()


def cerrarDocumento():
    valor = messagebox.askretrycancel(
        "Reintentar", "No es posible. Cerrar documento bloqueado")
    if valor == True:
        root.destroy()


# Primero creamos una variable donde se almacenara nuestro menu
barraMenu = Menu(root)

# Ahora usamos el metodo config para configurar nuestro menu
root.config(menu=barraMenu, width=300, height=300)
# Despues nos fijamos en los elementos que tendra nuestro menu o sus componentes

# ----------------Asi es como definimos los compoenetes de nuestro menu-----------
archivoMenu = Menu(barraMenu, tearoff=0)

# --------------Agregando elementos a las barras de menu-----------------------
# ----Lo hacemos con el metodo add_command---------------------------------

archivoMenu.add_command(label='Nuevo')
archivoMenu.add_command(label='Guardar')
archivoMenu.add_command(label='Guardar como')
# --------Agregar la barra que separa las subopciones de nuestro menu----------
# ---lo hacemos con la opion add_separator()------------------------------------
archivoMenu.add_separator()
archivoMenu.add_command(label='Cerrar', command=cerrarDocumento)
archivoMenu.add_command(label='Salir', command=salirAplicacion)


archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label='Copiar')
archivoEdicion.add_command(label='Cortar')
archivoEdicion.add_command(label='Pegar')

archivoHerramientas = Menu(barraMenu, tearoff=0)

archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label='Licencia', command=avisoLicencia)
archivoAyuda.add_command(label='Hacerca del programa', command=infoAdicional)
# --------------Vamos a darle un label a nuestras opciones de menu con
# el metodo add_cascade() usando su parametro label y el metodo menu

barraMenu.add_cascade(label='Archivos', menu=archivoMenu)
barraMenu.add_cascade(label='Edicion', menu=archivoEdicion)
barraMenu.add_cascade(label='Herramientas', menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()
