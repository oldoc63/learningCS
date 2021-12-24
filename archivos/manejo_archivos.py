try:
    archivo = open('prueba.txt','w', enconding='utf8')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Fin del archivo')

