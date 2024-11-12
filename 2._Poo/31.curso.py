# Uso de la libreria abc y su metodo abstractmethod
# La abstraccion consiste en ocultar la complejidad interna de un sistema
from abc import ABC, abstractmethod


class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f'Hola, me llamo: {self.nombre} y tengo {self.edad} años')

# Las clases abstractas no se pueden crear


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Estoy estudiando : {self.actividad}')


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Actualmente estoy trabajando en el rublo de: {self.actividad}')


mas_onewe = Estudiante('Mas', 27, 'Masculino', 'Programación')
pedro_mas = Trabajador('Pedro', 25, 'Masculino', 'Programación')
mas_onewe.presentarse()
mas_onewe.hacer_actividad()
pedro_mas.presentarse()
pedro_mas.hacer_actividad()
# mas_onewe.trabajar()  # Ahora también puedes llamar a trabajar()

# En nuestro ejemplo el metodo hacer_actividad() pasa a ser nuestro metodo abstracto
