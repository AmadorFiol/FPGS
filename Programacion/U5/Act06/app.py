'''
Pokedex
'''
import pygame, sys
from pygame.locals import *
#Esta libreria es la que me permite realizar la conexion con la pokeapi
#Es posible que necesites instalarla, para ello usa pip install requests
import requests

#-----Constantes-----#
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
LIGTHBLUE=(52, 204, 255)

#-----Definir clase-----#
class Pokemon(pygame.sprite.Sprite):  
    
    def __init__(self,numPokedex,nombre,tipo,img,desc,*groups):
        super().__init__(*groups)
        self.numPokedex=numPokedex
        self.nombre=nombre
        self.tipo=tipo
        self.img=img
        self.desc=desc

#-----Declaramos variables-----#
pokedex={}

#-----Declaramos funciones-----#
def download_pokemons():
    #Vamos a cargar solo la pokedex de la primera generacion
    #que consta de 151 pokemons
    url="https://pokeapi.co/api/v2/pokemon"
    for i in range(1,16):
        response=(requests.get(f"{url}/{i}")) #Realizamos la peticion
        data=response.json() #Hacemos que la informacion sea en formato json
        pokedex[data['id']]=Pokemon(
            data['id'], #Numero de Pokedex
            data['name'],
            [tipo['type']['name'] for tipo in data['types']], #Tipos, bucle comprimido por si ahi 2 tipos
            data['sprites']['front_default'],
            get_descPokemon(i)
            )
    return pokedex


def get_descPokemon(numPokedex):
    #Para obtener la descripcion debemos ir a otro endpoint,
    #el proposito de esta funcion es simplemente para poder
    #recoger dicha descripcion de dicho endpoint
    url="https://pokeapi.co/api/v2/pokemon-species"
    response=(requests.get(f"{url}/{numPokedex}"))
    data=response.json()
    return (data['flavor_text_entries'][0]['flavor_text'])

def next_Pokemon(numPokedex):
    if numPokedex==151:
        return pokedex[1]
    else:
        return pokedex[numPokedex+1]

def previous_Pokemon(numPokedex):
    if numPokedex==1:
        return pokedex[151]
    else:
        return pokedex[numPokedex-1]

#----Main----#
def main():
    pokedex=download_pokemons()
    actualPokemon=pokedex[1]

    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pokedex")
    fps=60
    pygame.key.set_repeat(1,int(1000/fps))
    sprites=pygame.sprite.Group()
    clock=pygame.time.Clock()

    #Bucle principal
    while True:
        screen.fill(LIGTHBLUE)
        clock.tick(fps)

        #Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                #Movimientos a traves de un input de tecla
                match(event.key):
                    case pygame.K_a | pygame.K_LEFT:
                        actualPokemon=previous_Pokemon(actualPokemon.numPokedex)
                    case pygame.K_d | pygame.K_RIGHT:
                        actualPokemon=next_Pokemon(actualPokemon.numPokedex)
        
        #Mostrar la imagen en el fondo y los sprites
        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()


if __name__=="__main__":
    main()