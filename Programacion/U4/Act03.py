'''
Crea una clase llamada Círculo que tenga los siguientes atributos:
- Radio
La clase debe tener un constructor que inicialice el atributo con el valor que se pase como parámetro.
La clase debe tener un método llamado calcular_área() y calcular_longitud() que calcule el área y la longitud del círculo y lo devuelva.
'''
class Radio():
    def __init__(self,radio):
        self.radio=radio

    def calcular_area(self):
        return 2**self.radio*3.14

    def calcular_long(self):
        return 2*3.14*self.radio
    
circuloNuevo=Radio(radio=int(input("Cual es el radio del circulo? ")))
print("El area es",circuloNuevo.calcular_area())
print("La longitud es",circuloNuevo.calcular_long())