from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'pyapp'
    _USERNAME = 'oldoc'
    _PASSWORD = 'leodoc754'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    
    @classmethod
    def obtenerPoll(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool')
                sys.exit()
        else:
            return cls._pool


    @classmethod
    def obtenerConexion(cls):
        pass
    
    

if __name__ == '__main__':
    pass