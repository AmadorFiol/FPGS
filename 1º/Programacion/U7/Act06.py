'''
Desarrolla una función llamada actualizar_película que reciba un objeto y
una cantidad variable de argumentos clave-valor para actualizar las propiedades del objeto.
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

def actualizar_pelicula(pelicula,**kwargs):
    for arg in kwargs:
        match(arg):
            case "titulo":
                pelicula.titulo=kwargs[arg]
            case "duracion":
                pelicula.duracion=kwargs[arg]
            case "actores":
                pelicula.actores=kwargs[arg]
            case _:
                pass

peli1=crear_pelicula("El Nombre","1:37","DiCaprio","Black Jack","La Roca")
peli2=crear_pelicula("El Nombre 2: la venganza","1:42","Black Jack","La Roca")
recuperar_pelicula(peli1)
actualizar_pelicula(peli1,duracion="1:39",titulo="The name")
recuperar_pelicula(peli1)