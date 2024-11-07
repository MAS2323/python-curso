# Codigo para abrir o leer los archivos del fichero
import pickle


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


ficheroApertura = open('losCoches', 'rb')
misCoches = pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:
    print(c.estado())