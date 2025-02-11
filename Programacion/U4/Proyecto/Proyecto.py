import os,random

# Error donde la posicion de los pokemon mostrada en la funcion
# Mapa.show_full_map() no coincide con la posicion de ese 
# pokemon

#-----Declaramos clases-----#
class Pokemon:
    def __init__(self,nombre,defensa,ataque,tipo):
        self.nombre=nombre
        self.defensa=defensa
        self.ataque=ataque
        self.tipo=tipo
        self.ps=100

    def AlmacenPokemon(nombre,pokemonsEnfrentados):
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

    def ataque_especial(self,rival):
        pass

class PokemonAgua(Pokemon):
    def __init__(self, nombre, defensa, ataque, tipo):
        super().__init__(nombre, defensa, ataque, tipo)
    
    def ataque_especial(self,rival):
        pass

class PokemonFuego(Pokemon):
    def __init__(self, nombre, defensa, ataque, tipo):
        super().__init__(nombre, defensa, ataque, tipo)
    
    def ataque_especial(self,rival):
        pass

class PokemonVolador(Pokemon):
    def __init__(self, nombre, defensa, ataque, tipo):
        super().__init__(nombre, defensa, ataque, tipo)
    
    def ataque_especial(self,rival):
        pass

class Mapa():
    def __init__(self,lado):
        self.casillas=[["-"] * lado for i in range(0,lado)]

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
                self.casillas[row][cell]=random.randint(0, len(almacen_pokemon)-2)

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
        #El jugador inicia con un bulbasaur, luego agregare la opcion de elegir el inicial
        self.team=[2]
        self.pokemonBox=[] #Lugar donde se almacenan los pokemons que no entran en el equipo

#-----Declaramos funciones-----#
def download_pokemon_list():
    with open("./pokedex.txt") as file:
        for line in file:
            newPokeInfo=line.split(",")
            match(newPokeInfo[1]):
                case "Fuego":
                    almacen_pokemon.append(PokemonFuego(newPokeInfo[0],int(newPokeInfo[2]),int(newPokeInfo[3]),newPokeInfo[1]))
                case "Agua":
                    almacen_pokemon.append(PokemonAgua(newPokeInfo[0],int(newPokeInfo[2]),int(newPokeInfo[3]),newPokeInfo[1]))
                case "Planta":
                    almacen_pokemon.append(PokemonPlanta(newPokeInfo[0],int(newPokeInfo[2]),int(newPokeInfo[3]),newPokeInfo[1]))
                case "Volador":
                    almacen_pokemon.append(PokemonVolador(newPokeInfo[0],int(newPokeInfo[2]),int(newPokeInfo[3]),newPokeInfo[1]))
    almacen_pokemon.append(Pokemon("Ninguno",0,0,"Ninguno"))

def change_pokemon():
    pokemon_changed=False
    while(not pokemon_changed):
        print("Que pokemon vas a sacar?")
        for i,pokemon in enumerate(player.team):
            print(f"{i}. {almacen_pokemon[pokemon].get_nombre()}")
            match(input("")):
                case "1":
                    if almacen_pokemon[0].get_ps()==0:
                        print("Este pokemon esta debilitado y no puede batallar")
                    else:
                        return player.team[0]
                case "2":
                    if almacen_pokemon[1].get_ps()==0:
                        print("Este pokemon esta debilitado y no puede batallar")
                    else:
                        return player.team[1]
                case "3":
                    if almacen_pokemon[2].get_ps()==0:
                        print("Este pokemon esta debilitado y no puede batallar")
                    else:
                        return player.team[2]
                case "4":
                    if almacen_pokemon[3].get_ps()==0:
                        print("Este pokemon esta debilitado y no puede batallar")
                    else:
                        return player.team[3]
                case "5":
                    if almacen_pokemon[4].get_ps()==0:
                        print("Este pokemon esta debilitado y no puede batallar")
                    else:
                        return player.team[4]
                case "6":
                    if almacen_pokemon[5].get_ps()==0:
                        print("Este pokemon esta debilitado y no puede batallar")
                    else:
                        return player.team[5]
                case _:
                    print("Esa no es una opcion valida")
                    os.system('pause')

def change_passedOut_pokemon():
    pokemon_changed=False
    while(not pokemon_changed):
        os.system('cls')
        print("Que pokemon vas a sacar?")
        for i,pokemon in enumerate(player.team):
            print(f"{i}. {almacen_pokemon[pokemon].get_nombre()}")
            print("X. Volver")
            match(input("")):
                case "1":
                    if almacen_pokemon[0].get_ps()==0:
                        print("Este pokemon esta debilitado y no puede batallar")
                        os.system('pause')
                        os.system('cls')
                    else:
                        return player.team[0]
                case "2":
                    if almacen_pokemon[1].get_ps()==0:
                        print("Este pokemon esta debilitado y no puede batallar")
                        os.system('pause')
                        os.system('cls')
                    else:
                        return player.team[1]
                case "3":
                    if almacen_pokemon[2].get_ps()==0:
                        print("Este pokemon esta debilitado y no puede batallar")
                        os.system('pause')
                        os.system('cls')
                    else:
                        return player.team[2]
                case "4":
                    if almacen_pokemon[3].get_ps()==0:
                        print("Este pokemon esta debilitado y no puede batallar")
                        os.system('pause')
                        os.system('cls')
                    else:
                        return player.team[3]
                case "5":
                    if almacen_pokemon[4].get_ps()==0:
                        print("Este pokemon esta debilitado y no puede batallar")
                        os.system('pause')
                        os.system('cls')
                    else:
                        return player.team[4]
                case "6":
                    if almacen_pokemon[5].get_ps()==0:
                        print("Este pokemon esta debilitado y no puede batallar")
                        os.system('pause')
                        os.system('cls')
                    else:
                        return player.team[5]
                case "X":
                        return False
                case _:
                    print("Esa no es una opcion valida")
                    os.system('pause')

def atack(atack,rival):
        damage=atack+10-rival.defensa 
        if damage<=0:
            damage=0
        rival.set_ps(rival.ps-damage)

        if rival.ps<0:
            rival.set_ps(0)
        return damage

def catch_pokemon(atack,rival):
    chance=(atack-rival.defensa)*(100-rival.ps)
    if random.randint(0,100)>chance:
        if len(player.team)<6:
            player.team.append(rival)
        else:
            player.pokemonBox.append(rival)
        return True

def pokemon_battle(x,y):
    rival=almacen_pokemon[map.casillas[y][x]]
    pokemon_in_battle=almacen_pokemon[player.team[0]]
    os.system('cls')
    while(rival.ps>0):
        action_made=False
        while(not action_made):
            print("Que vas a hacer?")
            print("1. Ataque basico")
            print("2. Cambiar pokemon")
            print("3. Capturar")
            print("4. Huir")
            print(f"\n{pokemon_in_battle.nombre}:{pokemon_in_battle.ps}\n{rival.nombre} rival:{rival.ps}")
            match(input("")):
                case "1":
                    atack_decided=False
                    while(not atack_decided):
                        print("Que ataque vas a hacer")
                        print("1. Ataque basico")
                        print("2. Ataque especial")
                        print("X. Volver")
                        match(input("")):
                            case "1":
                                damage=atack(pokemon_in_battle.ataque,rival)
                                print(f"Tu {pokemon_in_battle.nombre} ha hecho {damage} de daño al {rival.nombre} rival")
                                atack_decided=True
                                action_made=True
                            case "2":
                                pokemon_in_battle.ataque_especial()
                                atack_decided=True
                                action_made=True
                            case "X":
                                atack_decided=True
                            case _:
                                print("Esa no es una opcion valida")
                        os.system('pause')
                        os.system('cls')
                    if rival.ps==0:
                        print(f"El {rival.nombre} se ha debilitado")
                        map.casillas[y][x]=len(almacen_pokemon)-1
                        os.system('pause')
                        return
                case "2":
                    if change_pokemon()!=False:
                        action_made=True
                        os.system('pause')
                        os.system('cls')
                    
                case "3":
                    if catch_pokemon(pokemon_in_battle.ataque,rival):
                        print(f"Enhorabuena, el {rival.nombre} ha sido capturado")
                        map.casillas[y][x]=len(almacen_pokemon)-1
                        action_made=True
                        os.system('pause')
                        os.system('cls')
                        return
                case "4":
                    action_made=True
                    return
                case _:
                    print("Esa no es una opcion valida")    

        damage=atack(rival.ataque,pokemon_in_battle)
        print(f"El {rival.nombre} rival ha hecho {damage} de daño a tu {pokemon_in_battle.nombre}")
        if pokemon_in_battle.ps==0:
            pokemon_in_battle=change_passedOut_pokemon()
    os.system('pause')

def user_moving():
    match(input("En que dirección te quieres mover?\n(Debes usar WASD para moverte o X para salir)\n").upper()):
        case "W":
            if player.y<0:
                player.mover_Arriba()
                return True
            else:
                print("Has chocado con un muro invisible")
                return False
        case "A":
            if player.x>0:
                player.mover_Izquierda()
                return True
            else:
                print("Has chocado con un muro invisible")
                return False
        case "S":
            if player.y>-4:
                player.mover_Abajo()
                return True
            else:
                print("Has chocado con un muro invisible")
                return False
        case "D":
            if player.x<4:
                player.mover_Derecha()
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
player=Jugador(0,0,"Amador")
almacen_pokemon=[]
#-----Main-----#
download_pokemon_list()
map.asignPokemons()
while(not salir):
    os.system('cls')
    print(f"Posicion actual de {player.nombre}: {player.x}:{player.y}")
    map.show_minimap((player.x,player.y))
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
            if almacen_pokemon[map.casillas[player.y][player.x]].nombre=="Ninguno":
                pass
            elif user_moved:
                print(f"Te has encontrado un {almacen_pokemon[map.casillas[player.y][player.x]].nombre} salvaje")
                match(input("Quieres combatirlo?(Y/N) ").upper()):
                    case "Y":
                        pokemon_battle(player.x,player.y)
                    case "N":
                        pass
                    case _:
                       print("Algo ha ido mal")
                       os.system('pause')
        case "2":
            map.show_cell_info(player.x,player.y)
            os.system('pause')
        case "3":
            map.show_coords_map()
            os.system('pause')
        case "4":
            print(f"Y:{player.y},X:{player.x}\n{map.casillas[player.y][player.x]}")
            map.show_full_map_info()
            os.system('pause')
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")