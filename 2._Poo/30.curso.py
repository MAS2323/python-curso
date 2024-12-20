# La Abstraccion: significa manejar la complejidad ocultando todos los datos inecesarios al programador o al usuario
# dejandole solo las funcionalidades relevantes
# La abstraccion consiste en ocultar la complejidad interna de un sistema
class Auto():

    def __init__(self) -> None:
        self._estado = 'apagado'

    def encender(self):
        self._estado = 'encendido'
        print('El auto esta encendido')

    # Metodo abstracto
    # Antes de conducir si el autho esta apagado de forma abstracta
    # llamaremos al metodo encender
    def conducir(self):
        if self._estado == 'apagado':
            self.encender()
        print('Conduciendo el auto')


mi_auto = Auto()  # instanciando la clase
mi_auto.conducir()
