# Excepciones
# Una excepcion es un error que cocurre en tiempo de ejecucion de un programa

def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multi(num1, num2):
    return num1 * num2


def divi(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return "Operacion erronea"


while True:
    try:
        op1 = int(input("Introduzca el primer numero: "))
        op2 = int(input("Introduzca el segundo numero: "))

        break

    except ValueError:
        print("Los valores introducidos no son correctos")
operacion = input(
    "Introduzca la operacion a realizar (suma, resta, multiplica, divide): ")

if operacion == "suma":
    print(suma(op1, op2))
elif operacion == "resta":
    print(resta(op1, op2))
elif operacion == "multiplica":
    print(multi(op1, op2))
elif operacion == "divide":
    print(divi(op1, op2))

else:
    print("Operacion no encontrada")
print("Operacion ejecutada. Continuacion de ejecucion del programa")

# En python podemos utilizar varios except de forma consecutiva para


def Divide():

    try:
        op1 = (float(input("Introdice el primer numero: ")))
        op2 = (float(input("Introduce el segundo numero: ")))

        print("La division es: " + str(op1/op2))
    except ValueError:

        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

# Cuando quieres que un codigo se ejecute de forma consecutive puedes introducirlo en una clausula finally
    finally:
        # Lo que se introduce dentro del finally se va ha ejecutar siempre
        print("Calculo finalizado")


Divide()
