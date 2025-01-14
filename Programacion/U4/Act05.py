#Crea un programa que cree una lista de coches.
#Cada coche debe tener los datos establecidos en la actividad anterior
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
listadoCoches=[
    #Coche(marca,modelo,potencia,color,matriculacion)
    Coche("Toyota","Corola",0,"Blanco",2022),
    Coche("Skoda","Fabia",0,"Gris",2018),
    Coche("Tesla","Cibertruck",0,"Gris",2023)
]
salir=False

#-----Declaramos funciones-----#
def seleccionar_coche():
    cocheSel=None
    while(cocheSel==None):
        for num,coche in enumerate(listadoCoches):
            print(f"{num+1}. {coche.marca} {coche.modelo}")
        userInput=int(input("Que coche vas a pillar? "))
        if(userInput-1 not in range(0,len(listadoCoches))):
            print("Esa opcion no esta en el listado")
        else:
            cocheSel=listadoCoches[userInput-1]
            return cocheSel

def add_coche():
    marca=input("De que marca es el coche? ")
    modelo=input("Que modelo es? ")
    color=input("De que color es? ")
    matriculacion=int(input("En que año se matriculo? "))

    listadoCoches.append(Coche(marca,modelo,0,color,matriculacion))

#-----Main-----#
cocheSel=seleccionar_coche()
os.system("cls")
while(salir==False):
    print("1. Mostrar información")
    print("2. Acelerar")
    print("3. Frenar")
    print("4. Revisar proxima ITV")
    print("5. Seleccionar otro coche")
    print("S. Salir")
    match(input("Que quieres hacer? ")):
        case "1":
            cocheSel.mostrar()
            os.system("pause")
        case "2":
            print(cocheSel.acelerar())
            os.system("pause")
        case "3":
            print(cocheSel.frenar())
            os.system("pause") 
        case "4":
            print(cocheSel.itv())
            os.system("pause")
        case "5":
            cocheSel=seleccionar_coche()
            os.system("pause")
        case "6":
            add_coche()
            os.system("pause")
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")
            os.system("pause")
    os.system("cls")