# Alcance de Variables (scope)

var_global = 'Variable Global'

def imprimir():
    #Acceder a una Variable Global para modificación
    global var_global
    print(f'Variable Global desde función: {var_global}')
    #Definir variable local
    var_local = 'variable local'
    print(f'Variable local desde función: {var_local}')
    #No se puede acceder a var_local fuera de la función
    #Pero si desde fucniones anidadas
    def funcion_anidada():
        print(f'variable local dentro de función anidada: {var_local}')
    #Debemos llamar a la función anidada para que se ejecute
    funcion_anidada()
    var_global = 'Nuevo valor variable global'


imprimir()
print(f'Variable Global fuera de la función: {var_global}')