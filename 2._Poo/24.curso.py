#
class Persona:
    def __init__(self, nombre, edad, nacionalidad):

        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print('Hola, estoy hablando un poco')


class Artista:
    def __init__(self, habilidad) -> None:
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f'Mi habilidad es: {self.habilidad}')

# Herencia multiple


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa


miArtista = Artista('cantar')

miArtista.mostrar_habilidad()
