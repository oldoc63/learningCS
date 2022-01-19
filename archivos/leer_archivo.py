archivo = open('prueba.txt', 'r', encoding='utf8')

#print(archivo.read())
#print(archivo.read(5))
#print(archivo.read(3))
# print(archivo.readline())
# print(archivo.readline())

#iterar el archivo
# for linea in archivo:
#     print(linea)

#leer lineas
# print(archivo.readlines()) #Retorna una lista
# print(archivo.readlines()[0])

#a - anexar información
archivo2 = open('copia.txt', 'a')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
