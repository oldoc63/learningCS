try:
    archivo = open('prueba.txt','w')
except Exception as e:
    print(e)
finally:
    archivo.close()
    
