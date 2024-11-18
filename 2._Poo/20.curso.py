# POO Herencia
# La herencia sirve para reutilizar codigo
# Sobre escritura de metoso, herencia simple y multiple
class Vehiculos():
    # Definiendo los metodos de la clase Vehiculos()
    # Metodo constructor
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    # metodos de nuestra clase
    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print('Marca: ', self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)


# Clase Furgoneta que hereda de la clase Vehiculos

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

# Clase Moto que hereda de la clase Vehiculos


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

# Clase VElectricos que hereda los metodos y propiedades de la clase Vehiculos


class VElectricos(Vehiculos):

    def __init__(self, marca, modelo):  # metodo constructor
        # Metodo super, nos permite heredar todas las variables y metodos de la clase madre
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

# Cada clase tiene que tener algo caracteristico, pero todos tienen
# que tener las caracteristicas de la clase padre


# instancia de la clase moto: el modelo y la marca lo hereda de la clase vehiculo
miMoto = Moto("Honda", "CBR")

miMoto.caballito()  # metodo exclusivo de la clase moto

miMoto.estado()

miFurgoneta = Furgoneta("Renault", "kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

# Herrencia multiples
# Si las dos clases que se heredan tienen
# construcctores la clase heredara el construcctor de la primer clase
# Podemos usar muchas clases, siempre daremos preferencia a la que este mas a la izquierda


class BicicletaElectrica(VElectricos, Vehiculos):
    # en este ejemplo podemos ver que esta clase BicicletaElectrica hereda el metodo constructor de la clase VElectricos
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)


miBici = BicicletaElectrica("sdjdsa", "vfdjdfs")
