'''
Crea una clase llamada Coche que tenga los siguientes atributos:
- marca: una cadena de caracteres
- modelo: una cadena de caracteres
- potencia: un número entero
- color: una cadena de caracteres
- matriculacion: número entero
- siguiente_revision: número entero
Define también los siguientes métodos:
- mostrar(): muestra los datos del coche
- acelerar(): incrementa la potencia del coche en 10 caballos
- frenar(): decrementa la potencia del coche en 10 caballos
- itv(): devuelve la fecha de la siguiente revisión teniendo en cuenta que se pasa la primera vez a los 4 años, después 2 años, otros 2 años y finalmente cada 1 año.
'''
import os
from datetime import date

#-----Declaramos clases-----#
class Coche():
    def __init__(self,marca,modelo,potencia,color,matriculacion,sigRev=None):
        self.marca=marca
        self.modelo=modelo
        self.potencia=potencia
        self.color=color
        self.matriculacion=matriculacion
        self.sigRev=sigRev
    
    def mostrar(self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,"\nPotencia:",self.potencia,"\nColor",self.color,"\nMatriculacion",self.matriculacion,"\nSuiguiente ITV en ",self.sigRev)

    def acelerar(self):
        self.potencia+=10
        return (f"Velocidad actual:{self.potencia}")

    def frenar(self):
        if self.potencia==0:
            return("El coche esta parado")
        else:
            self.potencia=self.potencia-10
            return (f"Velocidad actual:{self.potencia}")

    def itv(self):
        actualYear=date.today().year
        antigüedadCoche=actualYear-self.matriculacion
        if antigüedadCoche<=4:
            self.sigRev=self.matriculacion+4
        elif(antigüedadCoche<8):
            self.sigRev=actualYear+2
        else:
            self.sigRev=actualYear+1
        return (f"La siguiente ITV se debe pasar en:{self.sigRev}")

#-----Declaramos variables-----#
salir=False

#-----Main-----#
marca=input("De que marca es el coche? ")
modelo=input("Que modelo es? ")
color=input("De que color es? ")
matriculacion=int(input("En que año se matriculo? "))

cocheNuevo=Coche(marca,modelo,0,color,matriculacion)
os.system("cls")
while(salir==False):
    print("1. Mostrar información")
    print("2. Acelerar")
    print("3. Frenar")
    print("4. Revisar proxima ITV")
    print("S. Salir")
    match(input("Que quieres hacer? ")):
        case "1":
            cocheNuevo.mostrar()
            os.system("pause")
        case "2":
            print(cocheNuevo.acelerar())
            os.system("pause")
        case "3":
            print(cocheNuevo.frenar())
            os.system("pause") 
        case "4":
            print(cocheNuevo.itv())
            os.system("pause")
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")
            os.system("pause")
    os.system("cls")