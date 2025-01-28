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
Cambios dictados por el profesor:
    nombre pasa a ser un atributo del Personaje
    Jugador ahora tiene el atributo nMovimientos
    Enemigo ahora tiene el metodo hablar()
    El mapa ahora es de 5x5
    Hacer cuando se encuentren iniciar la pelea
    Crear GUI basica mostrando el mapa
'''
import os,random
#-----Declaramos clases-----#
class Personaje():
    def __init__(self,x,y,nombre):
        self.x=x
        self.y=y
        self.nombre=nombre
        self.salud=100
        self.defensa=5
        self.ataque=0

    def mover_Derecha(self):
        self.x+=1
    
    def mover_Izquierda(self):
        self.x-=1

    def mover_Arriba(self):
        self.y+=1

    def mover_Abajo(self):
        self.y-=1

    def atacar(self,personaje):
        self.ataque=random.randint(0,10)
        daño=self.ataque-personaje.defensa 
        if daño<=0:
            daño=0
        personaje.salud=personaje.salud-daño

        if personaje.salud<0:
            personaje.salud=0
        return daño

class Jugador(Personaje):
    def __init__(self, x, y,nombre):
        super().__init__(x, y,nombre)
        self.nMovimientos=0

class Enemigo(Personaje):
    def __init__(self, x, y):
        super().__init__(x, y,"slime")
    
    def hablar(self):
        return "Buruburuburuburu"
    
#-----Declaramos variables-----#
j1=Jugador(0,0,"Amador")
slime=Enemigo(random.randint(-3,4),random.randint(-3,4))

#-----Declaramos funciones-----#
def show_mapa(posicionJugador):
    y=-3
    for i in range(0,len(range(-3,4))):
        for j in range(0,len(range(-3,4))):
            print("|-----|",end="")
        print("")
        x=-3
        for j in range(0,len(range(-3,4))):
            
            if posicionJugador==(x,y*-1):
                print("|  x  |",end="")
            else:
                print("|     |",end="")
            x+=1
        y+=1
        print("")

#-----Main-----#
while(j1.x!=slime.x and j1.y!=slime.y): #Bucle de movimiento por el mapa
    os.system("cls")
    print(f"Posicion actual de {j1.nombre}: {j1.x}:{j1.y}\nCantidad de movimientos realizados: {j1.nMovimientos}")
    show_mapa((j1.x,j1.y))
    match(input("En que dirección te quieres mover? (Debes usar WASD)\n").upper()):
        case "W":
            if j1.y<3:
                j1.mover_Arriba()
                j1.nMovimientos+=1
            else:
                print("Has chocado con un muro invisible")
                os.system("pause")
        case "A":
            if j1.x>-3:
                j1.mover_Izquierda()
                j1.nMovimientos+=1
            else:
                print("Has chocado con un muro invisible")
                os.system("pause")
        case "S":
            if j1.y>-3:
                j1.mover_Abajo()
                j1.nMovimientos+=1
            else:
                print("Has chocado con un muro invisible")
                os.system("pause")
        case "D":
            if j1.x<3:
                j1.mover_Derecha()
                j1.nMovimientos+=1
            else:
                print("Has chocado con un muro invisible")
                os.system("pause")
        case _:
            print("Esa no es una opcion valida")
            os.system("pause")
print(f"Posicion actual de {j1.nombre}: {j1.x}:{j1.y}")

print(f"Te has encontrado con un {slime.nombre}!\n El slime ataca! {slime.hablar()}")
os.system("pause")
while(j1.salud>0 and slime.salud>0): #Bucle de combate
    os.system("cls")
    print("Que comience el combate!")
    daño=j1.atacar(slime)
    if daño==0:
        print("El slime a esquivado el ataque")
    else:
        print(f"{j1.nombre} ataca\nHa hecho {daño} de daño al slime enemigo")

    if slime.salud==0:
        print(f"\n{j1.nombre} ha derrotado al slime enemigo")
        print(f"\nVida de {j1.nombre}: {j1.salud}     Vida del slime: {slime.salud}")
        break

    daño=slime.atacar(j1)
    if daño==0:
        print(f"{j1.nombre} a esquivado el ataque")
    else:
        print(f"El slime enemigo ataca\nHa hecho {daño} de daño al jugador {j1.nombre}")

    print(f"\nVida de {j1.nombre}: {j1.salud}     Vida del slime: {slime.salud}")
    
    if j1.salud==0:
        print(f"\nEl slime enemigo ha derrotado a {j1.nombre}")
        break
    os.system("pause")