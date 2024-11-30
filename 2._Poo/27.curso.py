# Getters y Setters
# Los usamos para acceder a variables o metodos encapsulados, los setter y getters nos permiten
# tener acceso a estos metodos

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    # Getter: nos permite acceder a un valor privado
    def get_nombre(self):
        return self.__nombre, self.__edad

    # Setter: nos permite modificar un valor privado
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre


miPersona = Persona('Antonio', 26)
print(miPersona.get_nombre())

miPersona.set_nombre('Ernesto')
print(miPersona.get_nombre())
