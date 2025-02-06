import os,random
#-----Declaramos clases-----#
class Pokemon:
    def __init__(self,nombre,defensa,ataque,tipo):
        self.nombre=nombre
        self.defensa=defensa
        self.ataque=ataque
        self.tipo=tipo
        self.ps=100

    def AlmacenPokemon(nombre,pokemonsEnfrentados): #Funcion que actua como almacen_pokemon
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
        self.casillas=[["-"] * lado for _ in range(lado)]

    def show_minimap(self,playerPosition):
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

    def show_cell_info(self,x,y):
        print(f"({x},{y}):{almacen_pokemon[self.casillas[y][x]].get_nombre()}")

    def show_coords_map(self):
        for row in range(0,len(self.casillas)): 
            for cell in range(0,len(self.casillas[row])):
                print(f"({cell}:{row*-1})",end="")
            print("")

    def show_full_map_info(self):
        for row in range(0,len(self.casillas)):
            for cell in range(0,len(self.casillas[row])):
                print(f"({cell}:{row*-1}):{almacen_pokemon[self.casillas[row][cell]].get_nombre()}, ",end="")
            print("")
    
    def asignPokemons(self):
        for row in range(0,len(self.casillas)): 
            for cell in range(0,len(self.casillas[row])):
                self.casillas[row][cell]=random.randint(0, len(almacen_pokemon)-1)

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
def pokemon_battle(x,y):
    pokemon_rival=almacen_pokemon[map.casillas[y][x]]
    os.system('cls')
    

def user_moving():
    match(input("En que dirección te quieres mover?\n(Debes usar WASD para moverte o X para salir)\n").upper()):
        case "W":
            if j1.y<0:
                j1.mover_Arriba()
                return True
            else:
                print("Has chocado con un muro invisible")
                return False
        case "A":
            if j1.x>0:
                j1.mover_Izquierda()
                return True
            else:
                print("Has chocado con un muro invisible")
                return False
        case "S":
            if j1.y>-4:
                j1.mover_Abajo()
                return True
            else:
                print("Has chocado con un muro invisible")
                return False
        case "D":
            if j1.x<4:
                j1.mover_Derecha()
                return True
            else:
                print("Has chocado con un muro invisible")
                return False
        case _:
            print("Esa no es una opcion valida")
            return False
#-----Declaramos variables-----#
salir=False
map=Mapa(5)
j1=Jugador(0,0,"Amador")
almacen_pokemon=[]
#El jugador inicia con un bulbasaur, luego agregare la opcion de elegir el inicial
team=[3]
#-----Main-----#
with open("./pokedex.txt") as file:
    for line in file:
        newPokeInfo=line.split(",")
        match(newPokeInfo[1]):
            case "Fuego":
                almacen_pokemon.append(PokemonFuego(newPokeInfo[0],newPokeInfo[2],newPokeInfo[3],newPokeInfo[1]))
            case "Agua":
                almacen_pokemon.append(PokemonAgua(newPokeInfo[0],newPokeInfo[2],newPokeInfo[3],newPokeInfo[1]))
            case "Planta":
                almacen_pokemon.append(PokemonPlanta(newPokeInfo[0],newPokeInfo[2],newPokeInfo[3],newPokeInfo[1]))
            case "Volador":
                almacen_pokemon.append(PokemonVolador(newPokeInfo[0],newPokeInfo[2],newPokeInfo[3],newPokeInfo[1]))

map.asignPokemons()
#-----Debugging-----#

#-----FIN DEBUG-----#

while(salir==False):
    os.system('cls')
    print(f"Posicion actual de {j1.nombre}: {j1.x}:{j1.y}")
    map.show_minimap((j1.x,j1.y))
    print("Que quieres hacer?")
    print("1. Moverse por el mapa")
    print("2. Ver informacion de la posicion actual")
    print("3. Mostrar mapa de coordenadas")
    print("4. Mostrar mapa completo")
    print("S. Salir")
    match(input("")):
        case "1":
            user_moved=user_moving()
            os.system('pause')
            if user_moved:
                print(f"Te has encontrado un {almacen_pokemon[map.casillas[j1.y][j1.x]].get_name()} salvaje")
                match(input("Quieres combatirlo?(Y/N) ").upper):
                    case "Y":
                        pass
                    case "N":
                        pass
                    case _:
                        pass
                pokemon_battle(j1.x,j1.y)
        case "2":
            map.show_cell_info(j1.x,j1.y)
            os.system('pause')
        case "3":
            map.show_coords_map()
            os.system('pause')
        case "4":
            map.show_full_map_info()
            os.system('pause')
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")