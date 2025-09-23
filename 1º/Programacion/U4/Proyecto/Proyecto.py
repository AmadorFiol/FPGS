import os,random

#-----Declaramos clases-----#
class Pokemon:
    def __init__(self,nombre,ataque,defensa,tipo):
        self.nombre=nombre
        self.defensa=defensa
        self.ataque=ataque
        self.tipo=tipo
        self.ps=100

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
    def __init__(self, nombre, ataque, defensa, tipo):
        super().__init__(nombre, ataque, defensa, tipo)

    def ataque_especial(self,rival):
        print(f"Tu {self.nombre} ha usado su ataque especial \"Megaton Floral\"")
        atack=self.ataque*get_type_advantage(self.tipo,rival.tipo)
        damage=atack+50-rival.defensa 
        if damage<=0:
            damage=0
        rival.set_ps(rival.ps-damage)

        if rival.ps<0:
            rival.set_ps(0)
        return damage

class PokemonAgua(Pokemon):
    def __init__(self, nombre, ataque, defensa, tipo):
        super().__init__(nombre, ataque, defensa, tipo)
    
    def ataque_especial(self,rival):
        print(f"Tu {self.nombre} ha usado su ataque especial \"Hidrovortice Abisal\"")
        atack=self.ataque*get_type_advantage(self.tipo,rival.tipo)
        damage=atack+50-rival.defensa 
        if damage<=0:
            damage=0
        rival.set_ps(rival.ps-damage)

        if rival.ps<0:
            rival.set_ps(0)
        return damage

class PokemonFuego(Pokemon):
    def __init__(self, nombre, ataque, defensa, tipo):
        super().__init__(nombre, ataque, defensa, tipo)
    
    def ataque_especial(self,rival):
        print(f"Tu {self.nombre} ha usado su ataque especial \"Hecatombe Pirica\"")
        atack=self.ataque*get_type_advantage(self.tipo,rival.tipo)
        damage=atack+50-rival.defensa 
        if damage<=0:
            damage=0
        rival.set_ps(rival.ps-damage)

        if rival.ps<0:
            rival.set_ps(0)
        return damage

class PokemonVolador(Pokemon):
    def __init__(self, nombre, ataque, defensa, tipo):
        super().__init__(nombre, ataque, defensa, tipo)
    
    def ataque_especial(self,rival):
        print(f"Tu {self.nombre} ha usado su ataque especial \"Picado Supersonico\"")
        atack=self.ataque*get_type_advantage(self.tipo,rival.tipo)
        damage=atack+50-rival.defensa 
        if damage<=0:
            damage=0
        rival.set_ps(rival.ps-damage)

        if rival.ps<0:
            rival.set_ps(0)
        return damage

class Mapa():
    def __init__(self,lado):
        self.lado=lado
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
        print(f"({x},{y*-1}):{almacenPokemon[self.casillas[y][x]].get_nombre()}")

    def show_coords_map(self):
        for row in range(0,len(self.casillas)): 
            for cell in range(0,len(self.casillas[row])):
                print(f"({cell}:{row*-1})",end="")
            print("")

    def show_full_map_info(self):
        for row in range(0,len(self.casillas)):
            for cell in range(0,len(self.casillas[row])):
                print(f"({cell}:{row*-1}):{almacenPokemon[self.casillas[row][cell]].get_nombre()}, ",end="")
            print("")
    
    def asign_pokemons(self):
        for row in range(0,len(self.casillas)): 
            for cell in range(0,len(self.casillas[row])):
                self.casillas[row][cell]=random.randint(0, len(almacenPokemon)-2)

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
        self.team=[]
        self.pokemonBox=[] #Lugar donde se almacenan los pokemons que no entran en el equipo

#-----Declaramos funciones-----#
def get_type_advantage(type,rivalType):
    match(type):
        case "Fuego":
            match(rivalType):
                case "Agua":
                    return 0.5
                case "Planta":
                    return 2
                case "Volador":
                    return 2
                case _:
                    return 1
        case "Agua":
            match(rivalType):
                case "Fuego":
                    return 2
                case "Planta":
                    return 0.5
                case _:
                    return 1
        case "Planta":
            match(rivalType):
                case "Fuego":
                    return 0.5
                case "Agua":
                    return 2
                case "Volador":
                    return 0.5
                case _:
                    return 1
        case "Volador":
            match(rivalType):
                case "Fuego":
                    return 0.5
                case "Planta":
                    return 2
                case _:
                    return 1

def download_pokemon_list():
    contadorFuego=0
    contadorAgua=0
    contadorPlanta=0
    contadorVolador=0
    with open("./pokedex.txt") as file:
        for line in file:
            newPokemonInfo=line.split(",")
            match(newPokemonInfo[1]):
                case "Fuego":
                    almacenPokemon.append(PokemonFuego(newPokemonInfo[0],int(newPokemonInfo[2]),int(newPokemonInfo[3]),newPokemonInfo[1]))
                    print(f"{newPokemonInfo[0]}, de tipo fuego, eficaz contra fuego y volador aunque debil contra agua")
                    contadorFuego+=1
                case "Agua":
                    almacenPokemon.append(PokemonAgua(newPokemonInfo[0],int(newPokemonInfo[2]),int(newPokemonInfo[3]),newPokemonInfo[1]))
                    print(f"{newPokemonInfo[0]}, de tipo agua, eficaz contra fuego aunque debil contra planta")
                    contadorAgua+=1
                case "Planta":
                    almacenPokemon.append(PokemonPlanta(newPokemonInfo[0],int(newPokemonInfo[2]),int(newPokemonInfo[3]),newPokemonInfo[1]))
                    print(f"{newPokemonInfo[0]}, de tipo planta, eficaz contra agua aunque debil contra fuego y volador")
                    contadorPlanta+=1
                case "Volador":
                    almacenPokemon.append(PokemonVolador(newPokemonInfo[0],int(newPokemonInfo[2]),int(newPokemonInfo[3]),newPokemonInfo[1]))
                    print(f"{newPokemonInfo[0]}, de tipo volador, eficaz contra planta aunque debil contra fuego")
                    contadorVolador+=1
            os.system('pause')
    almacenPokemon.append(Pokemon("Ninguno",0,999,"Ninguno"))
    os.system('cls')
    print(f"Se han cargado {contadorFuego} pokemons de tipo fuego")
    print(f"Se han cargado {contadorAgua} pokemons de tipo agua")
    print(f"Se han cargado {contadorPlanta} pokemons de tipo planta")
    print(f"Se han cargado {contadorVolador} pokemons de tipo volador")
    os.system('pause')
    os.system('cls')

#No hay control de errores en cuanto que pasaria si el jugador
#escoge una de las opciones en las que no hay pokemon
def change_pokemon():
    pokemonChanged=False
    while(not pokemonChanged):
        print("Que pokemon vas a sacar?")
        for i,pokemon in enumerate(player.team):
            print(f"{i+1}. {pokemon.get_nombre()}")
        print("X. Volver")
        match(input("")):
            case "1":
                if player.team[0].get_ps()==0:
                    print("Este pokemon esta debilitado y no puede batallar")
                else:
                    pokemonChanged=True
                    return player.team[0]
            case "2":
                if player.team[1].get_ps()==0:
                    print("Este pokemon esta debilitado y no puede batallar")
                else:
                    pokemonChanged=True
                    return player.team[1]
            case "3":
                if player.team[2].get_ps()==0:
                    print("Este pokemon esta debilitado y no puede batallar")
                else:
                    pokemonChanged=True
                    return player.team[2]
            case "4":
                if player.team[3].get_ps()==0:
                    print("Este pokemon esta debilitado y no puede batallar")
                else:
                    pokemonChanged=True
                    return player.team[3]
            case "5":
                if player.team[4].get_ps()==0:
                    print("Este pokemon esta debilitado y no puede batallar")
                else:
                    pokemonChanged=True
                    return player.team[4]
            case "6":
                if player.team[5].get_ps()==0:
                    print("Este pokemon esta debilitado y no puede batallar")
                else:
                    pokemonChanged=True
                    return player.team[5]
            case "X"|"x":
                pokemonChanged=True
                return False
            case _:
                print("Esa no es una opcion valida")
        os.system('pause')
        os.system('cls')

'''
Esta funcion es para comprobar si el jugador tiene aun algun pokemon que pueda sacar a pelear
tras la derrota de algun otro de sus pokemons, en caso de que tenga se hara que llame a la funcion
de change_passedOut_pokemon. En caso de que no tener pokemons disponibles para el combate este 
terminara de manera forzada
'''
def check_pokemon_able_battle():
    for pokemon in player.team:
        if pokemon.ps>0:
            return True
    return False

#No hay control de errores en cuanto que pasaria si el jugador
#escoge una de las opciones en las que no hay pokemon
def change_passedOut_pokemon():
    pokemonChanged=False
    while(not pokemonChanged):
        print("Que pokemon vas a sacar?")
        for i,pokemon in enumerate(player.team):
            print(f"{i+1}. {pokemon.get_nombre()}")
        match(input("")):
            case "1":
                if player.team[0].get_ps()==0:
                    print("Este pokemon esta debilitado y no puede batallar")
                else:
                    pokemonChanged=True
                    return player.team[0]
            case "2":
                if player.team[1].get_ps()==0:
                    print("Este pokemon esta debilitado y no puede batallar")
                else:
                    pokemonChanged=True
                    return player.team[1]
            case "3":
                if player.team[2].get_ps()==0:
                    print("Este pokemon esta debilitado y no puede batallar")
                else:
                    pokemonChanged=True
                    return player.team[2]
            case "4":
                if player.team[3].get_ps()==0:
                    print("Este pokemon esta debilitado y no puede batallar")
                else:
                    pokemonChanged=True
                    return player.team[3]
            case "5":
                if player.team[4].get_ps()==0:
                    print("Este pokemon esta debilitado y no puede batallar")
                else:
                    pokemonChanged=True
                    return player.team[4]
            case "6":
                if player.team[5].get_ps()==0:
                    print("Este pokemon esta debilitado y no puede batallar")
                else:
                    pokemonChanged=True
                    return player.team[5]
            case _:
                print("Esa no es una opcion valida")
        os.system('pause')
        os.system('cls')

def atack(yourPokemon,rival):
        atack=yourPokemon.ataque*get_type_advantage(yourPokemon.tipo,rival.tipo)
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
    rival=almacenPokemon[map.casillas[y][x]]
    pokemonInBattle=player.team[0]
    os.system('cls')
    while(rival.ps>0):
        actionMade=False
        while(not actionMade):
            print("Que vas a hacer?")
            print("1. Atacar")
            print("2. Cambiar pokemon")
            print("3. Capturar")
            print("4. Huir")
            print(f"\n{pokemonInBattle.nombre}:{pokemonInBattle.ps}\n{rival.nombre} rival:{rival.ps}")
            match(input("")):
                case "1": #Atacar
                    atackDecided=False
                    while(not atackDecided):
                        print("Que ataque vas a hacer")
                        print("1. Ataque basico")
                        print("2. Ataque especial")
                        print("X. Volver")
                        match(input("")):
                            case "1": #Ataque Basico
                                damage=atack(pokemonInBattle,rival)
                                print(f"Tu {pokemonInBattle.nombre} ha hecho {damage} de daño al {rival.nombre} rival")
                                atackDecided=True
                                actionMade=True
                            case "2":
                                damage=pokemonInBattle.ataque_especial(rival)
                                print(f"Tu {pokemonInBattle.nombre} ha hecho {damage} de daño al {rival.nombre} rival")
                                atackDecided=True
                                actionMade=True
                            case "X"|"x":
                                atackDecided=True
                            case _:
                                print("Esa no es una opcion valida")
                        os.system('pause')
                        os.system('cls')
                    if rival.ps==0: #Rival debilitado
                        print(f"El {rival.nombre} se ha debilitado")
                        rival.set_ps(100)
                        map.casillas[y][x]=len(almacenPokemon)-1
                        os.system('pause')
                        return
                case "2": #Cambio de pokemon
                    pokemonChosed=change_pokemon()
                    if pokemonChosed!=False:
                        pokemonInBattle=pokemonChosed
                        actionMade=True
                        os.system('pause')
                        os.system('cls')
                    
                case "3": #Capturar pokemon
                    if catch_pokemon(pokemonInBattle.ataque,rival):
                        print(f"Enhorabuena, el {rival.nombre} ha sido capturado")
                        map.casillas[y][x]=len(almacenPokemon)-1
                        actionMade=True
                        os.system('pause')
                        os.system('cls')
                        return
                    else:
                        print(f"El {rival.nombre} ha escapado de la pokeball")
                        actionMade=True
                        os.system('pause')
                        os.system('cls')

                case "4": #Huir
                    actionMade=True
                    print("Has huido del combate")
                    os.system('pause')
                    return
                case _:
                    print("Esa no es una opcion valida")    

        #Turno del rival
        damage=atack(rival,pokemonInBattle)
        print(f"El {rival.nombre} rival ha hecho {damage} de daño a tu {pokemonInBattle.nombre}")

        #Si te debilitan un pokemon
        if pokemonInBattle.ps==0:
            if check_pokemon_able_battle():
                pokemonInBattle=change_passedOut_pokemon()
            else:
                print("Ya no te quedan pokemons capazes de continuar el combate")
                print("Has tenido que ir huir del combate")
                os.system('pause')
                return
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
            if player.y>((map.lado-1)*-1):
                player.mover_Abajo()
                return True
            else:
                print("Has chocado con un muro invisible")
                return False
        case "D":
            if player.x<(map.lado-1):
                player.mover_Derecha()
                return True
            else:
                print("Has chocado con un muro invisible")
                return False
        case _:
            print("Esa no es una opcion valida")
            return False
        
def choose_starter_pokemon():
    startedChosed=False
    while(not startedChosed):
        os.system('cls')
        print(f"Escoge tu inicial {player.nombre}")
        print("1. Charmander")
        print("2. Bulbasaur")
        print("3. Squirtle")
        match(input("")):
            case "1":
                player.team.append(PokemonFuego("Charmander",52,43,"Fuego"))
                print("Has elegido a Charmander")
                startedChosed=True
            case "2":
                player.team.append(PokemonPlanta("Bulbasaur",49,49,"Planta"))
                print("Has elegido a Bulbasaur")
                startedChosed=True
            case "3":
                player.team.append(PokemonAgua("Squirtle",48,65,"Agua"))
                print("Has elegido a Squirtle")
                startedChosed=True
            case _:
                print("Esa no es una opcion valida")
        os.system('pause')
#-----Declaramos variables-----#
salir=False
map=Mapa(5)
player=Jugador(0,0,"")
almacenPokemon=[]
#-----Main-----#
download_pokemon_list()
map.asign_pokemons()
player.nombre=input("Cual es tu nombre? ")
choose_starter_pokemon()
while(not salir):
    os.system('cls')
    print(f"Posicion actual de {player.nombre}: {player.x}:{player.y}")
    map.show_minimap((player.x,player.y))
    print("Que quieres hacer?")
    print("1. Moverse por el mapa")
    print("2. Ver informacion de la posicion actual")
    print("3. Mostrar mapa de coordenadas")
    print("4. Mostrar mapa completo")
    print("5. Curar tus pokemons")
    print("S. Salir")
    match(input("")):
        case "1":
            user_moved=user_moving()
            os.system('pause')
            if almacenPokemon[map.casillas[player.y*-1][player.x]].nombre=="Ninguno":
                pass
            elif user_moved:
                print(f"Te has encontrado un {almacenPokemon[map.casillas[player.y*-1][player.x]].nombre} salvaje")
                match(input("Quieres combatirlo?(Y/N) ").upper()):
                    case "Y":
                        pokemon_battle(player.x,player.y*-1)
                    case "N":
                        pass
                    case _:
                       print("Algo ha ido mal")
                       os.system('pause')
        case "2":
            map.show_cell_info(player.x,player.y*-1)
            os.system('pause')
        case "3":
            map.show_coords_map()
            os.system('pause')
        case "4":
            map.show_full_map_info()
            os.system('pause')
        case "5":
            for pokemon in player.team:
                pokemon.set_ps(100)
            print("Tus pokemons han sido curados")
            os.system('pause')
        case "S"|"s":
            salir=True
        case _:
            print("Esa no es una opcion valida")
            os.system('pause')