'''
Hacer que el cuadrado se mueva segun entradas de teclado (WASD)
'''
import pygame
from pygame.locals import *
import sys

#-----Constantes-----#
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)

#-----Definir clase-----#
class Pad(pygame.sprite.Sprite):
    def __init__(self, pos,*groups):
        super().__init__(*groups)
        self.image=pygame.Surface((12,60)).convert()
        self.image.fill((WHITE))
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
        self.pos=pos
        self.image=pygame.Surface((10,10)).convert()
        self.image.fill((WHITE))
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

    def reset(self):
        self.rect=self.image.get_rect(center=self.pos)

class Score(pygame.sprite.Sprite):
    def __init__(self, font, pos=(0,0),*groups):
        super().__init__(*groups)
        self.font=font
        self.pos=pos
        self.score=0
        self.image=self.font.render(str(self.score), 0, WHITE)
        self.rect=self.image.get_rect(center=self.pos)
    
    def score_up(self):
        self.score+=1

    def update(self):
        self.image=self.font.render(str(self.score), 0, WHITE)
        self.rect=self.image.get_rect(center=self.pos)


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
    background=pygame.image.load("./background.png").convert()
    leftPad=Pad((SCREEN_WIDTH/6, SCREEN_HEIGHT/4))
    rigthPad=Pad((5*SCREEN_WIDTH/6, 3*SCREEN_HEIGHT/4))
    ball=Ball((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    font=pygame.font.Font('./wendy.ttf', 90)
    leftScore=Score(font,(SCREEN_WIDTH/3,SCREEN_HEIGHT/8))
    rigthScore=Score(font,(2*SCREEN_WIDTH/3,SCREEN_HEIGHT/8))
    sprites=pygame.sprite.Group(leftPad,rigthPad,ball,leftScore,rigthScore)
    clock=pygame.time.Clock()
    top=pygame.Rect(0,0,SCREEN_WIDTH,5)
    bottom=pygame.Rect(0,SCREEN_HEIGHT-5,SCREEN_WIDTH,5)
    left=pygame.Rect(0,0,5,SCREEN_HEIGHT)
    rigth=pygame.Rect(SCREEN_WIDTH-5,0,5,SCREEN_HEIGHT)

    #Bucle principal
    while True:
        clock.tick(fps)
        leftPad.stop()
        rigthPad.stop()

        #Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                #Movimientos a traves de un input de tecla
                match(event.key):
                    case pygame.K_w:
                        leftPad.move_up()
                    case pygame.K_s:
                        leftPad.move_down()
                    case pygame.K_UP:
                        rigthPad.move_up()
                    case pygame.K_DOWN:
                        rigthPad.move_down()
                    case pygame.K_SPACE:
                        ball.start(5,2)
            
            if ball.rect.colliderect(top) or ball.rect.colliderect(bottom):
                ball.change_y()
            elif ball.rect.colliderect(leftPad.rect) or ball.rect.colliderect(rigthPad.rect):
                ball.change_x()

            screenRect=screen.get_rect().inflate(0,-10)
            leftPad.rect.clamp_ip(screenRect)
            rigthPad.rect.clamp_ip(screenRect)

        if ball.rect.colliderect(left):
            rigthScore.score_up()
            ball.reset()
            ball.stop()
        elif ball.rect.colliderect(rigth):
            leftScore.score_up()
            ball.reset()
            ball.stop()
        
        
        #Mostrar la imagen en el fondo y los sprites
        sprites.update()
        screen.blit(background,(0,0))
        sprites.draw(screen)
        pygame.display.flip()


if __name__=="__main__":
    main()