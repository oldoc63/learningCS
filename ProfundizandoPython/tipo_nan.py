import math
from decimal import Decimal

# NaN - No a number (no es un número)
# NaN no es sensible a mayusculas/minusculas
# NaN es un tipo de dato numérico indefinido
a = float('NaN')
#print(f'a: {a}')
#print(f'Es NaN (not a number)?: {math.isnan(a)}')

#Usando el modulo decimal
a = Decimal('Nan')
print(f'a: {a}')
print(f'Es NaN (not a number)?: {math.isnan(a)}')
