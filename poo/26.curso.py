# Polimorfismo
# Se emplea cuando hay varias clases que realizan el mismo metodo y se llama de la misma forma
class Gato:
    def sonido(self):
        return 'Miau'


class Perro:
    def sonido(self):
        return 'Guau'

# Definiendo el polimorfismo


def hacer_sonido(animal):
    print(animal.sonido())


gato = Gato()
perro = Perro()

hacer_sonido(perro)
