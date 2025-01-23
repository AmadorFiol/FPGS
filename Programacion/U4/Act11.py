'''
Crea una clase Persona con atributos como nombre y edad.
Luego, crea una clase Empleado que herede de Persona y tenga un atributo adicional para el salario.
Comprueba su funcionamiento imprimiendo los atributos de un empleado.
'''
#-----Declaramos clases-----#
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

class Empleado(Persona):
    def __init__(self, nombre, edad,salario):
        super().__init__(nombre, edad)
        self.salario=salario
#-----Declaramos variables-----#
empleado1=Empleado("Juan",30,50000)
#-----Main-----#
print(f"Nombre: {empleado1.nombre}, Edad:{empleado1.edad}, Salario{empleado1.salario}")