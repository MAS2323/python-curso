# POO Polimorfismo (muchas formas)
# El polimorfismo en programacion quiere decir que un objeto puede cambiar de forma dependiendo del contexto
# en el que se utilice
class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")


class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")


class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")


# en este ejemplo el metodo desplazamiento es polimorfo:
# ya que lo tienen varias clases pero lo aplican de diferentes formas

# funcion poliforma
def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Moto()

desplazamientovehiculo(miVehiculo)

miCamion = Camion()

desplazamientovehiculo(miCamion)
