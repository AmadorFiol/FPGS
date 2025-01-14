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
    def __init__(self):
        pass
    def atacar(self,personaje):
        pass