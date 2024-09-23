# Condicionales
# If
# Operadores de comparacion <, >, <=, >=, ==, !=
print("Programa de evaluacion de notas de alumnos")

nota_alumno = int(input("Introuce la nota del alumno: "))


def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion


resultado = evaluacion(nota_alumno)
print(resultado)
