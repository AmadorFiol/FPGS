'''
Crea un método del objeto película que te permita extraer la información que contiene. 
Posteriormente crea una función recuperar_pelicula que reciba una cantidad variable de
objetos películas y devuelva la infomación de cada una de ellas. 
Previamente deberás crear esos objetos.
'''
class Pelicula:
    def __init__(self,titulo,duracion,actores):
        self.titulo=titulo
        self.duracion=duracion
        self.actores=actores

def crear_pelicula(titulo,duracion,*actores):
    return Pelicula(titulo,duracion,actores)

def recuperar_pelicula(*peliculas):
    for pelicula in peliculas:
        print(f"Titulo: {pelicula.titulo}\nDuracion: {pelicula.duracion}\nActores:")
        for actor in pelicula.actores:
            print(f"   {actor}")
        print("\n")

peli1=crear_pelicula("El Nombre","1:37","DiCaprio","Black Jack","La Roca")
peli2=crear_pelicula("El Nombre 2: la venganza","1:42","Black Jack","La Roca")
recuperar_pelicula(peli1,peli2)