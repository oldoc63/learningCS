#Las funciones en python son ciudadanas de primera clase
#First Class Citizens

# Definimos la funcion
def sumar( a, b):
    return a + b

# 1. Asignar la función a una variable (no se usan parentesis)
my_funcion = sumar

# Verificar el typo de variable
print(type(my_funcion))

# Llamamos la funcion a traves de la variable
resultado = my_funcion(5, 8)
print(f'Resultado: {resultado}')