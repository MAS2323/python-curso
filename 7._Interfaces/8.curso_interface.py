# el widget Menu
from tkinter import *

root = Tk()

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
archivoMenu.add_command(label='Cerrar')
archivoMenu.add_command(label='Salir')


archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label='Copiar')
archivoEdicion.add_command(label='Cortar')
archivoEdicion.add_command(label='Pegar')

archivoHerramientas = Menu(barraMenu, tearoff=0)

archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label='Hacerca del programa')
archivoAyuda.add_command(label='Licencia')
# --------------Vamos a darle un label a nuestras opciones de menu con
# el metodo add_cascade() usando su parametro label y el metodo menu

barraMenu.add_cascade(label='Archivos', menu=archivoMenu)
barraMenu.add_cascade(label='Edicion', menu=archivoEdicion)
barraMenu.add_cascade(label='Herramientas', menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()
