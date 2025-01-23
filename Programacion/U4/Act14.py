'''
Crea una clase base llamada Personaje con los atributos de una posición en el mapa X, Y.
También tendrán los métodos
moverDerecha(): sumará una posición a X
moverIzquierda(): restará una posición a X
moverArriba(): Sumará una posición a Y
moverAbajo(): Restará una posición a Y
Crea dos clases derivadas llamadas Jugador y Enemigo que desciendan de Personaje,
define algún atributo interesante como su nombre por ejemplo.
Crea dos objetos, uno para Jugador y otro para Enemigo.
Coloca al objeto enemigo en una posición del mapa (define x e y)
Crea un bucle para mover al jugador hasta encontrar al enemigo.
Cada paso que dé el jugador, debe aparecer por pantalla
Si el enemigo choca contra el jugador, éste perderá la partida.
'''
import os,random
#-----Declaramos clases-----#
class Personaje():
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
    def __init__(self, x, y, nombre):
        super().__init__(x, y)
        self.nombre=nombre

class Enemigo(Personaje):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.nombre="Slime"
    
#-----Declaramos variables-----#
j1=Jugador(0,0,"Amador")
slime=Enemigo(random.randint(-10,11),random.randint(-10,11))
#-----Main-----#
while(j1.x!=slime.x and j1.y!=slime.y):
    print(f"Posicion actual de {j1.nombre}: {j1.x}:{j1.y}")
    match(input("En que dirección te quieres mover? (Debes usar WASD)\n").upper()):
        case "W":
            if j1.y<10:
                j1.mover_Arriba()
            else:
                print("Has chocado con un muro invisible")
                os.system("pause")
        case "A":
            if j1.x>-10:
                j1.mover_Izquierda()
            else:
                print("Has chocado con un muro invisible")
                os.system("pause")
        case "S":
            if j1.y>-10:
                j1.mover_Abajo()
            else:
                print("Has chocado con un muro invisible")
                os.system("pause")
        case "D":
            if j1.x<10:
                j1.mover_Derecha()
            else:
                print("Has chocado con un muro invisible")
                os.system("pause")
        case _:
            print("Esa no es una opcion valida")
            os.system("pause")
    os.system("cls")
print(f"Posicion actual de {j1.nombre}: {j1.x}:{j1.y}")
print(f"Te has encontrado con un {slime.nombre}")
