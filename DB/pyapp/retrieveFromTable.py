import psycopg2

try:
    conexion = psycopg2.connect(
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
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = '''
            SELECT city FROM weather
            WHERE temp_lo = (SELECT max(temp_lo) FROM weather);
            '''
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()