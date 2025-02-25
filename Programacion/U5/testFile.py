import pygame
from pygame.locals import *
import sys

#-----Constantes-----#
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

#-----Main-----#
def main():
    pygame.init()
    #Creacion y titulacion de la ventana
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("tutorial pygame parte 2")

    #Bucle principal
    while True:
        #Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()