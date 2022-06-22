# Funciones Anidadas

def calculadora(a, b, operacion='sumar'):
    # 1. Definir Funcion anidada
    def sumar(a, b):
       return a + b

    def restar(a, b):
        return a - b

    # 2. Llamar funcion anidada
    if operacion == 'sumar':
        print(f'Resultado de sumar: {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Resultado de restar: {restar(a, b)}')

calculadora(5, 6)
calculadora(4, 3, operacion='restar')