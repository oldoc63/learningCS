resultado = None
a = '10'
b = 0

try:
    resultado = a/b
except ZeroDivisionError as e:
    print(f'Ocurrió un error: {e}')

print(f'Resultado: {resultado}')
print('Continuamos ... ')
