# Decoradores
# En python una funcion decorador es una funcion que decora a otra
# Son usados para validacion de sesiones, la medicion del tiempo de jecucion etc.

def decorador(function):
    def funcion_modificada():
        print('Antes de llamar a la funcion')
        function()
        print('Despues de llamar la funcion')
    return funcion_modificada


# def saludo():
#     print('Hola Mundo')


# saludo_modificado = decorador(saludo)
# saludo_modificado()
@decorador
def saludo():
    print('Hola Mas como andas')


saludo()
