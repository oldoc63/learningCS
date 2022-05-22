# Manejo de valores infinitos
import math
from decimal import Decimal

infinito_positivo = float('inf')
#print(f'Infinito Positivo: {infinito_positivo}')
#print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = float('-inf')
#print(f'infinito_negativo: {infinito_negativo}')
#print(f'Es infinito?: {math.isinf(infinito_negativo)}')

# Infinito con atributo .inf
infinito_positivo = math.inf
#print(f'Infinito Positivo: {infinito_positivo}')
#print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
#print(f'infinito_negativo: {infinito_negativo}')
#print(f'Es infinito?: {math.isinf(infinito_negativo)}')

#Módulo Decimal
infinito_positivo = Decimal('Infinity')
print(f'Infinito Positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = Decimal('-Infinity')
print(f'infinito_negativo: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')