'''
Pokedex
'''
import pygame, sys, random
from pygame.locals import *
#Esta libreria es la que me permite realizar la conexion con la pokeapi
#Es posible que necesites instalarla, para ello usa pip install requests
import requests

#Esta libreria me permite usar imagenes online
from io import BytesIO

#-----Constantes-----#
SCREEN_WIDTH=477
SCREEN_HEIGHT=941
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
LIGTHBLUE=(52, 204, 255)

#-----Definir clase-----#
class Pokemon(pygame.sprite.Sprite):   
    def __init__(self,numPokedex,nombre,tipos,image,desc,lv,*groups):
        super().__init__(*groups)
        self.numPokedex=numPokedex
        self.nombre=nombre
        if len(tipos)==2:
            self.tipo=tipos[0]+" "+tipos[1]
        else:
            self.tipo=tipos[0]
        self.desc=desc
        self.lv=lv
        self.image=BytesIO(image)
        self.image=pygame.image.load(self.image).convert_alpha()
        self.rect=self.image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))

#-----Declaramos variables-----#
pokedex={}

#-----Declaramos funciones-----#
def download_pokemons():
    #Vamos a cargar solo la pokedex de la primera generacion
    #que consta de 151 pokemons
    #Al final usando solo los 15 primeros pq sino son demasiados y peta
    url="https://pokeapi.co/api/v2/pokemon"
    for i in range(1,16):
        response=(requests.get(f"{url}/{i}")) #Realizamos la peticion
        data=response.json() #Hacemos que la informacion sea en formato json
        pokedex[data['id']]=Pokemon(
            data['id'], #Numero de Pokedex
            data['name'],
            [tipo['type']['name'] for tipo in data['types']], #Bucle comprimido por si ahi 2 tipos
            requests.get(data['sprites']['front_default']).content, #Imagen
            get_descPokemon(i),
            random.randint(1,100)
            )
    return pokedex


def get_descPokemon(numPokedex):
    #Para obtener la descripcion debemos ir a otro endpoint,
    #el proposito de esta funcion es simplemente para poder
    #recoger dicha descripcion de dicho endpoint
    url="https://pokeapi.co/api/v2/pokemon-species"
    response=(requests.get(f"{url}/{numPokedex}"))
    data=response.json()
    for entrie in data['flavor_text_entries']:
        if entrie['language']['name']=="es":
            desc=change_certain_chars(entrie['flavor_text'])
    return desc

#Hay algunos caracteres que no se detectan correctamente
#por pygame y los cambia por !, aqui cambio esos
#caracteres por los correspondientes
def change_certain_chars(text):
    desc=""
    for char in text:
        match (char):
            case "\n":
                desc+=" "
            case "á":
                desc+="a"
            case "é":
                desc+="e"
            case "í":
                desc+="i"
            case "ó":
                desc+="o"
            case "ú":
                desc+="u"
            case _:
                desc+=char
    return desc

#Funcion realizada por GPT para poder realizar salto de linea
#en el momento en el que el texto llegue al limite de su cuadro
def draw_wrapped_text(surface, text, rect, font, color):
    words = text.split(" ")  # Dividir el texto en palabras
    lines = []
    current_line = ""

    for word in words:
        # Probar si la palabra cabe en la línea actual
        test_line = current_line + word + " "
        test_width, _ = font.size(test_line)

        if test_width < rect.width:
            current_line = test_line  # Agregar palabra
        else:
            lines.append(current_line)  # Guardar línea y empezar otra
            current_line = word + " "  # Nueva línea con la palabra actual

    lines.append(current_line)  # Agregar última línea

    # Dibujar cada línea con separación vertical
    y_offset = 0
    for line in lines:
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (rect.x + 10, rect.y + 10 + y_offset))
        y_offset += font.get_height()

def next_Pokemon(numPokedex):
    if numPokedex==15:
        return pokedex[1]
    else:
        return pokedex[numPokedex+1]

def previous_Pokemon(numPokedex):
    if numPokedex==1:
        return pokedex[15]
    else:
        return pokedex[numPokedex-1]

#----Main----#
def main():
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pokedex")
    pokedex=download_pokemons()
    actualPokemon=pokedex[1]
    background=pygame.image.load("./background.jpg").convert()
    FONT=pygame.font.Font("./wendy.ttf", 20)
    descFont=pygame.font.Font("./wendy.ttf",32)
    descRect=pygame.Rect(30, SCREEN_HEIGHT/2, 400, 50) #(x, y, ancho, alto)
    typeRect=pygame.Rect(30, SCREEN_HEIGHT/4, 100, 50)
    lvRect=pygame.Rect(SCREEN_WIDTH-100, SCREEN_HEIGHT/4, 100, 50)

    sprites=pygame.sprite.Group(actualPokemon)

    #Bucle principal
    while True:
        #Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                #Movimientos a traves de un input de tecla
                match(event.key):
                    case pygame.K_a:
                        actualPokemon=previous_Pokemon(actualPokemon.numPokedex)
                    case pygame.K_d:
                        actualPokemon=next_Pokemon(actualPokemon.numPokedex)
            
        sprites=pygame.sprite.Group(actualPokemon)
        
        #Mostrar la image en el fondo y los sprites
        sprites.update()
        screen.blit(background,(0,0))
        draw_wrapped_text(screen, actualPokemon.desc, descRect, descFont, BLACK)
        draw_wrapped_text(screen, f"Tipos: {actualPokemon.tipo}", typeRect, FONT, BLACK)
        draw_wrapped_text(screen, f"Lv.{actualPokemon.lv}", lvRect, FONT, BLACK)
        sprites.draw(screen)
        pygame.display.flip()


if __name__=="__main__":
    main()