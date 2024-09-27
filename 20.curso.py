# POO Herencia
# La herencia sirve para reutilizar codigo
# Sobre escritura de metoso, herencia simple y multiple
class Vehiculos():

    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print('Marca: ', self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)


class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


class Moto(Vehiculos):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    # Sobre escritura del metodo estado
    def estado(self):
        print('Marca: ', self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena, "\n",
              self.hcaballito
              )


class VElectricos():

    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

# Cada clase tiene que tener algo caracteristico, pero todos tienen
# que tener las caracteristicas de la clase padre


miMoto = Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta = Furgoneta("Renault", "kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

# Herrencia multiples
# Si las dos clases que se heredan tienen
# construcctores la clase heredera heredara el construcctor de la primer clase
# Podemos usar muchas clases, siempre daremos preferencia a la que este mas a la izquierda


class BicicletaElectrica(VElectricos, Vehiculos):
    pass


miBici = BicicletaElectrica()
