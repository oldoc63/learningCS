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
   SELECT city, (temp_hi+temp_lo)/2 AS temp_avg, date FROM weather;
    '''
    cursor.execute(sentencia)
    print('data retrieved')
except:
    print('failed to retrieve data')

registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()
