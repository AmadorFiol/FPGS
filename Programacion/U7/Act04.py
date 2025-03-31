'''
Escribe una función llamada crear_peliculas que reciba la información
básica de una película (título, duración, actores, etc.) y cree los objetos.
Primero deberás crear el objeto película con su constructor.
'''
class Pelicula:
    def __init__(self,titulo,duracion,actores):
        self.titulo=titulo
        self.duracion=duracion
        self.actores=actores

def crear_pelicula(titulo,duracion,*actores):
    return Pelicula(titulo,duracion,actores)

peli1=crear_pelicula("El Nombre","1:37","DiCaprio","Black Jack","La Roca")