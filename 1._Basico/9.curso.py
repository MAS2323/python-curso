# Condicionales

salario_precidente = int(input("Introduzca el salario del precidente: "))
print("Salario presidente: " + str(salario_precidente))

salario_director = int(input("Introduzca el salario del diretor: "))
print("Salario del director: " + str(salario_director))

salario_jefe_area = int(input("Introduzca el salario del jefe de area: "))
print("Salario jefe de area: " + str(salario_jefe_area))

salario_administrativo = int(
    input("Introduzca el salario del administrativo: "))
print("Salario presidente: " + str(salario_administrativo))

# Condicional de evaluacion
# Concatenacion de operadores de comparacion
if salario_administrativo < salario_jefe_area < salario_director < salario_precidente:
    print('Todo ofunciona correctamente')
else:
    print('Algo falla en esta empresa')
