from NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('numeros identicos')
    resultado = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {e}, {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {e}, {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {e}, {type(e)}')
else:
    print('No se arrojó ninguna excepción')
finally:
    print('Ejecución del bloque finally')
print(f'Resultado: {resultado}')
print('Continuamos ...')
