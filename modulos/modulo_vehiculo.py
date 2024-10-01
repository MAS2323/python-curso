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


class VElectricos(Vehiculos):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True
