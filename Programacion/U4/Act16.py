'''
Vamos a crear un sistema simple de cuentas bancarias utilizando programación orientada a objetos en Python.
Crea las siguientes clases:

CuentaBancaria (Clase CuentaBancaria):
Una clase base que representa una cuenta bancaria básica.
Debe contener los siguientes métodos:
Inicializar la cuenta
Obtener el saldo
Depositar dinero
Retirar dinero (manejando con control de errores)
Transferir dinero a otra cuenta (también controlando errores).

CuentaRecompensas (Subclase de CuentaBancaria):
Una subclase de CuentaBancaria que proporciona una recompensa de interés del 5% en los depósitos que hayan ingresado.

CuentaAhorros (Subclase de CuentaBancaria:
Una subclase de CuentaBancaria que agrega una tarifa de retiro de 5€ en cada transacción de retiro.
'''
import os
#-----Declaramos clases-----#
class CuentaBancaria:
    def __init__(self,saldoInicial,nombre):
        self.saldo=saldoInicial
        self.nombre=nombre

    def get_saldo(self):
        return self.saldo

    def depositar_dinero(self,ingreso):
        self.saldo+=ingreso

    def retirar_dinero(self,retiro):
        if retiro<=self.saldo and retiro>0:
            self.saldo-=retiro
            return True
        else:
            return False

    def transferencia(self,saldo,cuentaDestino):
        if self.retirar_dinero(saldo):
            cuentaDestino.depositar_dinero(saldo)
            return True
        else:
            return False

class CuentaRecompensas(CuentaBancaria):
    def __init__(self, saldoInicial, nombre):
        super().__init__(saldoInicial, nombre)

    def depositar_dinero(self, ingreso):
        self.saldo+=(ingreso+(self.saldo*(5/100)))

class CuentaAhorros(CuentaBancaria):
    def __init__(self, saldoInicial, nombre):
        super().__init__(saldoInicial, nombre)

    def retirar_dinero(self, retiro):
        if retiro<=self.saldo and retiro>0:
            self.saldo-=(5+retiro)
            return True
        else:
            return False
#-----Declaramos variables-----#
salir=False
cuentas={}
#-----Declaramos funciones-----#
def crear_cuenta(nombre,saldoInicial):
    print("Que tipo de cuenta quieres crear?")
    print("1. Cuenta basica")
    print("2. Cuenta de recompensas")
    print("3. Cuenta de ahorros")
    print("V. Volver")
    match(input("")):
        case "1":
            cuentas[nombre]=CuentaBancaria(saldoInicial,nombre)
        case "2":
            cuentas[nombre]=CuentaRecompensas(saldoInicial,nombre)
        case "3":
            cuentas[nombre]=CuentaAhorros(saldoInicial,nombre)
        case "V":
            return
#-----Main-----#
while(salir==False):
    os.system("cls")
    print("Que quieres hacer?")
    print("1. Crear cuenta")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Realizar transferencia")
    print("5. Mostrar saldo")
    print("S. Salir")
    match(input("")):
        case "1":
            nombre=input("Cual es el nombre de la cuenta? ")
            saldo=int(input("Cual es el saldo inicial? "))
            if nombre not in cuentas and saldo>0:
                crear_cuenta(nombre,saldo)
            elif saldo<=0:
                print("El saldo inicial debe ser mayor a 0")
            else:
                print("Ya existe esta cuenta")

        case "2":
            nombre=input("A que cuenta vas a ingresar el dinero? ")
            saldo=int(input("Cuanto vas a ingresar? "))
            if nombre in cuentas and saldo>0:
                cuentas[nombre].depositar_dinero(saldo)
            elif saldo<=0:
                print("El deposito debe ser mayor a 0")
            else:
                print("La cuenta no existe")

        case "3":
            nombre=input("A que cuenta vas a retirar dinero? ")
            saldo=int(input("Que tanto vas a retirar? "))
            if nombre in cuentas:
                if not cuentas[nombre].retirar_dinero(saldo):
                    print("No hay suficiente saldo en la cuenta")
            else:
                print("La cuenta no existe")
        
        case "4":
            nombre=input("Que cuenta realizara la transferencia? ")
            cuentaDestino=input("A que cuenta se va a transferir el dinero? ")
            saldo=int(input("Que tanto dinero se va a transferir? "))
            if nombre in cuentas and cuentaDestino in cuentas:
                if cuentas[nombre].transferencia(saldo,cuentas[cuentaDestino]):
                    print("La transferencia se ha completado")
                else:
                    print("No hay suficiente saldo para realizar la transferencia")
            elif nombre not in cuentas:
                print("La cuenta origen no existe")
            else:
                print("La cuent destino no existe")
        case "5":
            nombre=input("De que cuenta quieres revisar el saldo? ")
            if nombre in cuentas:
                print(f"El saldo de {nombre} es de {cuentas[nombre].saldo}")
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")
    os.system("pause")