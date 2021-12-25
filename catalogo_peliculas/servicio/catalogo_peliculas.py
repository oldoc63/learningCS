class CatalogoPeliculas:

    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            