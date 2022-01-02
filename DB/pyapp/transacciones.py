import psycopg2 as bd

try:
    conexion = bd.connect(
        user='oldoc',
        password='leodoc754',
        host='127.0.0.1',
        port='5432',
        database='pyapp'
)
    print("connected to the database")
except:
    print("unable to connect to the database")

print(conexion)

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Karla', 'Gomez','kgomez@mail.com')
    cursor.execute(sentencia, valores)
    conexion.commit()
    print('Termina la transaccion')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo rollback {e}')
finally:
    conexion.close()
