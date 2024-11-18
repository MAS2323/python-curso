# La funcion map aplica una funcion a cada elemento de una lista iterable (listas, tuplas etc) devolviendo una lista
# con los resultados

class Empleados:

    # metodo constructor
    def __init__(self, nombre, cargo, salario) -> None:
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo

    # funcion str

    def __str__(self):
        return "{} que trabajo como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)

# Creacion de una lista


lista_empleados = [

    Empleados('Vicencio', 'Director', 7800),
    Empleados('Mas', 'Ingeniero', 6000),
    Empleados('Consuelo', 'Administrativo', 3500),
    Empleados('Ernesto', 'Inspector', 3000),
    Empleados('Mario', 'Electricista', 4400)
]

# creamos la funcion que hara el calculo de la comision


def calculoComision(empleado):
    # devolvera el slario de los empleados mas un 3% del mismo

    if (empleado.salario <= 3000):

        empleado.salario = empleado.salario*1.03

    return empleado


# en esta lista se almacenaran todos los valores de la funcion map
# el primer argumento de la funcion map es otra funcion, encargada de hacer el calculo
# el segundo argumento es la lista que le pasaremos a la funcion para que haga el calculo
listaEmpleadosComision = map(calculoComision, lista_empleados)

for empleados in listaEmpleadosComision:

    print(empleados)
