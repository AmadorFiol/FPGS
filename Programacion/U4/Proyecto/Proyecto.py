import os,random
#-----Declaramos clases-----#
class Pokemon:
    def __init__(self,nombre,defensa,ataque,tipo):
        self.nombre=nombre
        self.defensa=defensa
        self.ataque=ataque
        self.tipo=tipo
        self.ps=100

    def AlmacenPokemon(nombre): #Funcion que actua como Pokedex
        pokemonsEnfrentados.append(nombre)

    def get_nombre(self):
        return self.nombre
    
    def get_defensa(self):
        return self.defensa
    
    def get_ataque(self):
        return self.ataque
    
    def get_tipo(self):
        return self.tipo
    
    def get_ps(self):
        return self.ps
    
    def set_ps(self,ps):
        self.ps=ps

    
#Para los ataques especiales de cada tipo voy a usar los Movimientos Z
#Mecanica especial introducida en la 7ª generacion (Pokemon Sol y Luna)
class PokemonPlanta(Pokemon):
    def __init__(self, nombre, defensa, ataque, tipo):
        super().__init__(nombre, defensa, ataque, tipo)

    def ataque_especial(self):
        pass

class PokemonAgua(Pokemon):
    def __init__(self, nombre, defensa, ataque, tipo):
        super().__init__(nombre, defensa, ataque, tipo)
    
    def ataque_especial(self):
        pass

class PokemonFuego(Pokemon):
    def __init__(self, nombre, defensa, ataque, tipo):
        super().__init__(nombre, defensa, ataque, tipo)
    
    def ataque_especial(self):
        pass

class PokemonVolador(Pokemon):
    def __init__(self, nombre, defensa, ataque, tipo):
        super().__init__(nombre, defensa, ataque, tipo)
    
    def ataque_especial(self):
        pass

class Mapa():
    def __init__(self,lado):
        self.casillas=[[""]*lado]*lado

    def show_realtime_map(self,playerPosition):
        y=0
        for row in self.casillas:
            for cell in row:
                print("|-----|",end="")
            print("")
            x=0
            for cell in row:  
                if playerPosition==(x,y*-1):
                    print("|  x  |",end="")
                else:
                    print("|     |",end="")
                x+=1
            y+=1
            print("")

    def show_cell(self,x,y):
        print(f"({x},{y}):{self.casillas[x][y]}")

    def asignPokemons(self):
        num=random.randint(0,25)
        for row in range(0,len(self.casillas)):
            for cell in range(0,row):
                while(cell==""):
                    if num not in self.casillas:
                        self.casillas[row][cell]=num
                    else:
                        num=random.randint(0,25)

class Personaje:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def mover_Derecha(self):
        self.x+=1
    
    def mover_Izquierda(self):
        self.x-=1

    def mover_Arriba(self):
        self.y+=1

    def mover_Abajo(self):
        self.y-=1

class Jugador(Personaje):
    def __init__(self, x, y,nombre):
        super().__init__(x, y)
        self.nombre=nombre

#-----Declaramos funciones-----#
def combat():
    pass

def user_moving():
    match(input("En que dirección te quieres mover?\n(Debes usar WASD para moverte o X para salir)\n").upper()):
        case "W":
            if j1.y<0:
                j1.mover_Arriba()
            else:
                print("Has chocado con un muro invisible")
        case "A":
            if j1.x>0:
                j1.mover_Izquierda()
            else:
                print("Has chocado con un muro invisible")
        case "S":
            if j1.y>-4:
                j1.mover_Abajo()
            else:
                print("Has chocado con un muro invisible")
        case "D":
            if j1.x<4:
                j1.mover_Derecha()
            else:
                print("Has chocado con un muro invisible")
        case _:
            print("Esa no es una opcion valida")
#-----Declaramos variables-----#
salir=False
pokemonsEnfrentados=()
mapa=Mapa(5)
j1=Jugador(0,0,"Amador")
pokedex=[]
equipo=[0,1,2,3,4,5,6]
#-----Main-----#
with open("pokedex.txt") as archivo:
    for linea in archivo:
        new=linea.split(",")
        pokedex.append(Pokemon(new[0],new[2],new[3],new[1]))
mapa.asignPokemons()
while(salir==False):
    os.system('cls')
    print(f"Posicion actual de {j1.nombre}: {j1.x}:{j1.y}")
    mapa.show_realtime_map((j1.x,j1.y))
    print("Que quieres hacer?")
    print("1. Moverse por el mapa")
    print("2. Ver informacion de la posicion actual")
    print("3. Mostrar mapa de coordenadas")
    print("4. Mostrar mapa completo")
    print("S. Salir")
    match(input("")):
        case "1":
            user_moving()
            os.system('pause')
        case "2":
            mapa.show_cell(j1.x,j1.y)
            os.system('pause')
        case "3":
            pass
        case "4":
            pass
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")