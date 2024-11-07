# Guardar archivos en nuestra computadora de forma permanente
import pickle

# El objetivo es mediante este codigo se vayan cargando la informacion en un fichero externo


class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print('Se ha creado una persona nueva con el nombre de:', self.nombre)

    # El metodo str lo que hace es convertir en cadena de texto la informacion de un objeto
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersona:

    personas = []

    def __init__(self):
        listaPersonas = open('ficheroExterno', 'ab+')
        listaPersonas.seek(0)  # Desplazar el cursor a la posicion cero

        try:
            self.personas = pickle.load(listaPersonas)
            print('Se cargaron {} personas del fichero externo'.format(
                len(self.personas)))
        except:
            print('El fichero esta vacio')

        finally:
            listaPersonas.close()
            del (listaPersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        ListaPersona = open('ficheroExterno', 'wb')
        pickle.dump(self.personas, ListaPersona)
        ListaPersona.close()
        del (ListaPersona)

    def mostrarInfoFicheroExterno(self):
        print('La informacion del fichero externo es la siguiente:')
        for p in self.personas:
            print(p)


miLista = ListaPersona()

persona = Persona('Ana', 'Femenino', 7)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()
