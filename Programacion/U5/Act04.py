'''
Hacer que el cuadrado se mueva segun entradas de teclado (WASD)
'''
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
    #-----Definir variables-----#
    x=0
    y=0

    pygame.init()
    #Creacion y titulacion de la ventana
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Actividad 1")

    #Bucle principal
    while True:
        screen.fill(BLACK)
        #Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                #Movimientos a traves de un input de tecla
                while (event.type==pygame.KEYDOWN):
                    match(event.key):
                        case pygame.K_w:
                            if y<=0:
                                y=0
                            else:
                                y-=10
                        case pygame.K_a:
                            if x<=0:
                                x=0
                            else:
                                x-=10
                        case pygame.K_s:
                            if y>=SCREEN_HEIGHT-100:
                                y=SCREEN_HEIGHT-100
                            else:
                                y+=10
                        case pygame.K_d:
                            if x>=SCREEN_WIDTH-100:
                                x=SCREEN_WIDTH-100
                            else:
                                x+=10
        
        #Dibujamos las figuras
        pygame.draw.rect(screen, RED, (x, y, 100, 100))
        pygame.draw.circle(screen, GREEN, (200, 200), 50)
        pygame.draw.polygon(screen, BLUE, [(300, 300), (350, 250), (400, 300)])
        pygame.draw.line(screen, (255, 255, 0), (100, 400), (400, 400), 5)
                    

        #Con esto hacemos que cada que acaba el bucle
        #se redibuje todo lo que debe redibujar
        pygame.display.update()



if __name__ == "__main__":
    main()