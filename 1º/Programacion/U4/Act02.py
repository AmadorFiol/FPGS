'''
Crea una clase llamada Rectángulo que tenga los siguientes atributos:
- Base
- Altura
La clase debe tener un constructor que inicialice los atributos con los valores que se pasen como parámetros.
La clase debe tener un método llamado calcular_área() que calcule el área del rectángulo y lo devuelva.
'''
class Rectangulo():
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    
    def calcular_area(self):
        return self.base*self.altura
    
base=int(input("Cual es la base? "))
altura=int(input("Cual es la altura? "))
rectanguloNuevo=Rectangulo(base,altura)
print(rectanguloNuevo.calcular_area())