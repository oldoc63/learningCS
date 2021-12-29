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

cursor = conexion.cursor()

try:
    sentencia = '''
   SELECT * FROM weather
    WHERE city = 'San Francisco' AND prcp > 0.0;
    '''
    cursor.execute(sentencia)
    print('data retrieved')
except:
    print('failed to retrieve data')

registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()
