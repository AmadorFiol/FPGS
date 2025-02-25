import pygame
from pygame.locals import *
import sys

#-----Constantes-----#
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)

#----Main----#
def main():
    pygame.init()
    #Creacion y titulacion de la ventana
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Actividad 1")

    #Bucle principal
    while True:
        #Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #Dibujamos las figuras
        pygame.draw.rect(screen, (255, 0, 0), ((SCREEN_WIDTH/2)-50, (SCREEN_HEIGHT/2)-50, 100, 100))
        pygame.draw.circle(screen, (0, 255, 0), (200, 200), 50)
        pygame.draw.polygon(screen, (0, 0, 255), [(300, 300), (350, 250), (400, 300)])
        pygame.draw.line(screen, (255, 255, 0), (100, 400), (400, 400), 5)

        #Con esto hacemos que cada que acaba el bucle
        #se redibuje todo lo que debe redibujar
        pygame.display.update()



if __name__ == "__main__":
    main()