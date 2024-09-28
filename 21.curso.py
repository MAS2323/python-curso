# La funcion super(): halla donde lo uses en tu codigo va a llamar al metodo padre

class Persona():

    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre  # self.nombre variables de clase
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    # metodos
    def descripcion(self):

        print("Nombre: ", self.nombre, " Edad: ", self.edad,
              " Residencia: ", self.lugar_residencia)


class Empleado(Persona):
    # Uso de la funcion super()
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "Antiguedad", self.antiguedad)


Antonio = Persona("Victoriano", 55, "Malaga")
Antonio.descripcion()

# Principio de sustitucion
# Cuando tenemos herencia un objeto de la subclase siempre sera un objeto de la supercase
# Ej: Un empleado es siempre una persona pero al reves no se da esta condicion

# En python tenemos la funcion isinstance() que nos va a informar siempre si un objeto es instancia de
# una clase determinada
print(isinstance(Antonio, Empleado))
