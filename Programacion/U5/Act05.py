'''
Hacer que el cuadrado se mueva segun entradas de teclado (WASD)
'''
import pygame
from pygame.locals import *
import sys

#-----Constantes-----#
SCREEN_WIDTH=1200
SCREEN_HEIGHT=600
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)

#-----Definir variables-----#
background=pygame.image.load("./background.png").convert

#-----Definir clase-----#
class Pad(pygame.sprite.Sprite):
    def __init__(self, pos,*groups):
        super().__init__(*groups)
        self.image=pygame.Surface((12,30)).convert().fill((WHITE))
        self.rect=self.image.get_rect(center=pos)
        self.maxSpeed=5
        self.speed=0

    def move_up(self):
        self.speed=self.maxSpeed*-1
        
    def move_down(self):
        self.speed=self.maxSpeed*1
        
    def stop(self):
        self.speed=0

    def update(self):
        self.rect.move_ip(0,self.speed)

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos,*groups):
        super().__init__(*groups)
        self.image=pygame.Surface((12,30)).convert().fill((WHITE))
        self.rect=self.image.get_rect(center=pos)
        self.speedX=0
        self.speedY=0
    
    def change_y(self):
        self.speedY*=-1
    
    def change_x(self):
        self.speedX*=-1
    
    def start(self,speedX,speedY):
        self.speedX=speedX
        self.speedY=speedY

    def stop(self):
        self.speedX=0
        self.speedY=0
    
    def update(self):
        self.rect.move_ip(self.speedX,self.speedY)


#----Main----#
def main():
    pygame.init()
    #Creacion y titulacion de la ventana
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Actividad 5")
    fps=60
    pygame.key.set_repeat(1,int(1000/fps))

    #-----VarLocales-----#
    y=0
    padLeft=Pad((SCREEN_WIDTH/6, SCREEN_HEIGHT/4))
    padRight=Pad((5*SCREEN_WIDTH/6, 3*SCREEN_HEIGHT/4))
    ball=Ball((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    sprites=pygame.sprite.Group(padLeft,padRight,ball)
    clock=pygame.time.Clock()
    top=pygame.Rect(0,0,SCREEN_WIDTH,5)
    bottom=pygame.Rect(0,SCREEN_HEIGHT-5,SCREEN_WIDTH,5)

    #Bucle principal
    while True:
        clock.tick(fps)
        padLeft.stop()
        padRight.stop()

        #Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                #Movimientos a traves de un input de tecla
                match(event.key):
                    case pygame.K_w:
                        if y<=0:
                            y=0
                        else:
                            y-=10
                    case pygame.K_s:
                        if y>=SCREEN_HEIGHT-100:
                            y=SCREEN_HEIGHT-100
                        else:
                            y+=10
                    case pygame.K_SPACE:
                        ball.start(0,0)

        
        #Con esto hacemos que cada que acaba el bucle
        #se redibuje todo lo que debe redibujar
        pygame.display.update()

        #Mostrar la imagen en el fondo y los sprites
        sprites.update()
        screen.blit(background,(0,0))
        sprites.draw(screen)
        screen.display.flip()


if __name__=="__main__":
    main()