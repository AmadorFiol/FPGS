'''
Crea una clase llamada Persona que tenga los siguientes atributos:
- Nombre
- Apellidos
- Edad
- Sexo
La clase debe tener un constructor que inicialice los atributos con los valores que se pasen como parámetros.
'''

class Persona():
    def __init__(self,nombre,apellidos,edad,sexo):
        self.nombre=nombre
        self.appellidos=apellidos
        self.edad=edad
        self.sexo=sexo

    def mostrar_info(self):
        print(self.nombre,self.appellidos,"\n",self.edad,"\n",self.sexo)

nombre=input("Cual es tu nombre? ")
apellidos=input("Cuales son tus apellidos? ")
edad=int(input("Cual es tu edad? "))
sexo=input("Cual es tu sexo? (M o F) ")

personaNueva=Persona(nombre,apellidos,edad,sexo)

personaNueva.mostrar_info()