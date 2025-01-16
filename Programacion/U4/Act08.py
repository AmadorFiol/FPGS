'''
Definir una clase llamada Personaje.

La clase Personaje debe tener los siguientes atributos:
nombre: una cadena de caracteres que representa el nombre del personaje.
salud: un número entero que representa la salud del personaje.
ataque: un número entero que representa el ataque del personaje.
defensa: un número entero que representa la defensa del personaje.

La clase Personaje debe tener los siguientes métodos:
init(): un método constructor que inicializa los atributos del personaje.
atacar(personaje): un método que ataca a otro personaje, reduciendo su salud.

Crear  dos objetos Personaje, uno para el jugador y otro para el enemigo.

Programa un bucle que permita al jugador atacar al enemigo y viceversa hasta que uno de los dos muera.

Debes utilizar la función randint() para generar números aleatorios que representen el daño causado por los ataques.
'''
import os,random
#-----Declaramos clases-----#
class Personaje():
    def __init__(self,nombre,salud,defensa):
        self.nombre=nombre
        self.salud=salud
        self.defensa=defensa
        self.ataque=0

    def atacar(self,personaje):
        self.ataque=random.randint(0,10)
        daño=self.ataque-personaje.defensa 
        if daño<=0:
            daño=0
        personaje.salud=personaje.salud-daño

        if personaje.salud<0:
            personaje.salud=0
        return daño

#-----Declaramos variables-----#
nombre=input("Cual sera el nombre de tu personaje? ")
j1=Personaje(nombre,100,5)
slime=Personaje("slime",100,5)

#-----Main-----#
while(j1.salud>0 and slime.salud>0):
    os.system("cls")

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