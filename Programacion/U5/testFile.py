# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame
from pygame.locals import *
import sys

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


# ------------------------------
# Funcion principal del juego
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("tutorial pygame parte 2")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = pygame.image.load("Miku.jpg").convert()
    tux = pygame.image.load("logoSJO.png").convert_alpha()

    tux_pos_x = 550
    tux_pos_y = 200

    # Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(tux, (tux_pos_x, tux_pos_y))
    screen.blit(fondo, (0, 0))
    # se muestran lo cambios en pantalla
    pygame.display.flip()

    # el bucle principal del juego
    while True:
        # le restamos 1 a la coordenada x de tux
        # asi se mueve un poquito a la izquierda
        tux_pos_x = tux_pos_x - 1
        screen.blit(tux, (tux_pos_x, tux_pos_y))
        # se muestran lo cambios en pantalla
        pygame.display.flip()

        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()