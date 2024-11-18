# Siempre vamos a usar la funcion filter para filtrar objetos

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

    Empleados('Vicencio', 'Director', 780000),
    Empleados('Mas', 'Ingeniero', 60000),
    Empleados('Consuelo', 'Administrativo', 35000),
    Empleados('Ernesto', 'Inspector', 30000),
    Empleados('Mario', 'Electricista', 44000)
]

# uso de la funcion filter y lambda
# la funcion filter solo mostrara los empleados cuyo salario es mayor a 50000
salarios_altos = filter(
    lambda empleado: empleado.salario > 50000, lista_empleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)
