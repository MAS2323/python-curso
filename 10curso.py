# Condicionales ejercicio
print("Asignaturas optativas 2017-2018")
print("Asignaturas Optativas: Informativo grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion = input("Escribe la asignatura escogida: ")

asignatura = opcion.lower()

if asignatura in ('informativo grafica', 'pruebas de software', 'usabilidad y accesibilidad'):

    print("Asignatura elegida " + asignatura)
else:

    print("La asignatura escogida no esta contemplada")
