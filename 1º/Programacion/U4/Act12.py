'''
Crea una clase base Animal con un método mover.
Luego, crea dos clases derivadas Pajaro y Pez que hereden de Animal y tengan métodos adicionales como volar y nadar respectivamente.
Además, a Pez deberás crearle su propio método mover para sobreescribir el general.
Añade un print a cada método para que se pueda observar su ejecución.
'''
#-----Declaramos clases-----#
class Animal:
    def __init__(self):
        pass

    def mover(self):
        print("El animal se ha movido")
    
class Pajaro(Animal):
    def __init__(self):
        super().__init__()

    def volar(self):
        print( "El pajaro esta volando")
    
class Pez(Animal):
    def __init__(self):
        super().__init__()

    def mover(self):
        print("El pez se esta moviendo")
    
    def nadar(self):
        print("El pez esta nadando")

#-----Declaramos variables-----#
pajaro=Pajaro()
pez=Pez()
#-----Main-----#
pajaro.mover()
pajaro.volar()
pez.mover()
pez.nadar()