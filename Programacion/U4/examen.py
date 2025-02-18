#-----Act 1-----#
class Cancion():
    def __init__(self,title,artist,year):
        self.title=title
        self.artist=artist
        self.year=year
        self.genre=""

    #-----Act 2----#
    def get_title(self):
        return self.title
    
    def get_artist(self):
        return self.artist
    
    def get_year(self):
        return self.year
    
    def get_genre(self):
        return self.genre
    
    def mostrar_info(self):
        print(f"Cancion: {self.title}, Artista: {self.artist}, Año: {self.year}, Genero: {self.genre}")

#-----Act 3----#
class Pop(Cancion):
    def __init__(self, title, artist, year):
        super().__init__(title, artist, year)
        self.genre="Pop"

class Rock(Cancion):
    def __init__(self, title, artist, year):
        super().__init__(title, artist, year)
        self.genre="Rock"

class Trap(Cancion):
    def __init__(self, title, artist, year):
        super().__init__(title, artist, year)
        self.genre="Trap"

#----Act 4 y 5 (dicen lo mismo)----#
cancionPop1=Pop("Pop1","CantantePop",1998)
cancionPop2=Pop("Pop2","CantantePop",2001)
cancionRock1=Rock("Rock1","CantanteRock",1999)
cancionRock2=Rock("Rock2","CantanteRock",2003)
cancionTrap1=Trap("Trap1","CantanteTrap",1997)
cancionTrap2=Trap("Trap2","CantanteTrap",2005)

listaCanciones=[cancionPop1,cancionPop2,cancionRock1,cancionRock2,cancionTrap1,cancionTrap2]

#-----Act 6-----#
def mostrar_canciones(lista):
    for cancion in lista:
        cancion.mostrar_info()

print("Act 6")
mostrar_canciones(listaCanciones)

#-----Act 7----#
def mostrar_canciones_nuevas(lista):
    for cancion in lista:
        if cancion.get_year()>2000:
            cancion.mostrar_info()
print("\nAct 7")
mostrar_canciones_nuevas(listaCanciones)
