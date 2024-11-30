# POO Programacion Orientada a Objetos

class Coche():  # Definicion de una clase
    # Caracteriscas de la clase Coche (propiedades)
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    # Comportamiento de nuestro objeto se determinan mediante metodos
    # Self hace referencia al propio objeto
    def arrancar(self):  # Metodo de nuestra clase
        self.enmarcha = True

    def estado(self):  # este metodo sirve para definir el estado de nuestra clase
        if (self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"


miCoche = Coche()  # Instanciar una clase
print("El largo del coche es: ", miCoche.anchoChasis)
print("El coche tien ", miCoche.ruedas, "ruedas")
# miCoche.arrancar()

print(miCoche.estado())
