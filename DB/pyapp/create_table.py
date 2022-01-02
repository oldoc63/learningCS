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
    CREATE TABLE cities (
        name     varchar(80) primary key,
        location point
);
    '''
    cursor.execute(sentencia)
    conexion.commit()
    print('table created')
except:
    print('failed to create tabled')
