# Decorador property

class Persona:
    def __init__(self, nombre, edad) -> None:
        # variables encapsuladas
        self.__nombre = nombre
        self._edad = edad

    @property  # Poder acceder al valor nombre
    def nombre(self):
        return self.__nombre

    @nombre.setter  # Poder modificar el valor nombre
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter  # Poder eliminar los valores
    def nombre(self):
        del self.__nombre


miPersona = Persona('Antonio', 26)


miNombre = miPersona.nombre
print(miNombre)


# Asignarle un valor a una de las variables de nuestra clase
miPersona.nombre = 'Victoriano'

# Acceder a las variables introducidas e imprimirlas por pantalla
miNombre2 = miPersona.nombre
print(miNombre2)

# Formas de eliminar un elemento de nuestros metodos
del miPersona.nombre
