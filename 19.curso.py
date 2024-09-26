# POO Programacion Orientada a Objetos
class Coche():
    # Estado inicaial de la clase
    # El construcctor es el metodo especial que le da estado inicial a los objetos

    def __init__(self):  # metodo constructor
        # Asi es como se encapsulan las variables, asi hacemos que esta variable no sea accesible desde el exterior de la clase
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if (self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif (self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar"
        else:
            "El coche esta parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, "y un largo de",
              self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "mal"
        self.puerta = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puerta == "cerradas"):
            return True
        else:
            return False


miCoche = Coche()
print(miCoche.arrancar(True))

miCoche.estado()
print("----------------A contnuacion creamos el segundo objeto---------------")

# Segunda instancia
miCoche2 = Coche()
print(miCoche2.arrancar(False))

miCoche2.estado()
