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
    INSERT INTO weather (city, temp_lo, temp_hi, prcp, date)
    VALUES ('San Francisco', 43, 57, 0.0, '1994-11-29');
    '''
    cursor.execute(sentencia)
    conexion.commit()
    print('table modified')
except:
    print('failed to modify table')
