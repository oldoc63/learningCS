# bool contiene los valores de True y False
# Tipos numéricos, False para 0, True demás valores

# valor = 0
# resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# Tipo str, False para '', True demás valores
# valor = ''
# resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# valor = 'hola'
# resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

#Tipo colecciones, False para colecciones vacias, True para todas las demas colecciones
#Lista
# valor = []
# resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# valor = [1,2,3]
# resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

#Tupla
# valor = ()
# resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# valor = 1,2,3
# resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

#Diccionarios
# valor = {}
# resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# valor = {'nombre':'leopoldo', 'apellido':'olmos'}
# resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

#Tipo bool y sentencias control

# if '':
#     print('Regresó verdadero')
# else:
#     print('Regresó falso')

# if bool(''):
#     print('Regresó verdadero')
# else:
#     print('Regresó falso')

# if 'hola':
#     print('Regresó verdadero')
# else:
#     print('Regresó falso')

# if bool('hola'):
#     print('Regresó verdadero')
# else:
#     print('regresó falso')

# if 0:
#     print('Regresó verdadero')
# else:
#     print('Regresó falso')

# if bool(0):
#     print('Regresó verdadero')
# else:
#     print('Regresó falso')

# if [1]:
#     print('Regresó verdadero')
# else:
#     print('Regresó falso')

# if {}:
#     print('Regresó verdadero')
# else:
#     print('Regresó falso')

# if {'name':'leopoldo', 'apellido':'olmos'}:
#     print('Regresó verdadero')
# else:
#     print('Regresó falso')

variable = ''
if variable:
    print('Regresó verdadero')
else:
    print('Regresó falso')

variable = 'hola'
if variable:
    print('Regresó verdadero')
else:
    print('Regresó falso')

#Using while

variable = ''
while variable:
    print('ejecución ciclo while')
else:
    print('fin ciclo while')

variable = 'hola'
while variable:
    print('ejecución ciclo while')
    break
else:
    print('fin ciclo while')