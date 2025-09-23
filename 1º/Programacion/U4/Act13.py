'''
Crea una clase base llamada Vehiculo que tenga los atributos comunes a todos los vehículos,
como el número de ruedas y la velocidad actual. Incluye un método para acelerar.
Luego crea una clase derivada llamada Coche que herede de Vehiculo.
Agrega un atributo adicional para el número de puertas.
Sobrescribe el método de acelerar para imprimir un mensaje específico para un coche.
Finalmente crea una clase derivada llamada Bicicleta que herede de Vehiculo.
Agrega un atributo adicional para el tipo de bicicleta (montaña, carretera, etc.).
Sobrescribe el método de acelerar para imprimir un mensaje específico para una bicicleta.
'''
#-----Declaramos clases-----#
class Vehiculo:
    def __init__(self,numRuedas,velocidadActual):
        self.numRuedas=numRuedas
        self.velocidadActual=velocidadActual

    def acelerar(self,aumento):
        self.velocidadActual+=aumento
        return f"La velocidad actual de la vehiculo es: {self.velocidadActual}"


class Coche(Vehiculo):
    def __init__(self, numRuedas, velocidadActual,numPuertas):
        super().__init__(numRuedas, velocidadActual)
        self.numPuertas=numPuertas
    
    def acelerar(self,aumento):
        self.velocidadActual+=aumento
        return f"La velocidad actual de la coche es: {self.velocidadActual}"
    
class Bicicleta(Vehiculo):
    def __init__(self, numRuedas, velocidadActual,tipo):
        super().__init__(numRuedas, velocidadActual)
        self.tipo=tipo

    def acelerar(self, aumento):
        self.velocidadActual+=aumento
        return f"La velocidad actual de la bici es: {self.velocidadActual}"
#-----Declaramos variables-----#
coche=Coche(4,30,2)
bici=Bicicleta(2,5,"Ciudad")
#-----Main-----#
print(coche.acelerar(20))
print(bici.acelerar(10))