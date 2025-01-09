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
class Coche():
    def __init__(self,marca,modelo,potencia,color,matriculacion,sigRev):
        self.marca=marca
        self.modelo=modelo
        self.potencia=potencia
        self.color=color
        self.matriculacion=matriculacion
        self.sigRev=sigRev
    
    def mostrar(self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,"\nPotencia:",self.potencia,"\nColor",self.color,"\nMatriculacion",self.matriculacion,"\nSuiguiente ITV en ",self.sigRev)

    def acelerar(self):
        pass

    def frenar(self):
        pass

    def itv(self):
        pass

cocheNuevo=Coche("Toyota","Corolla",100,"Blanco",2025,4)
cocheNuevo.mostrar()