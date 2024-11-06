#Crear un minijuego de adivinar un num del 1 al 100 y con 10 intentos usando bucle While
import random
intentos=10
numAdivinar=random.randint(1,100)
numInput=0
while numInput!=numAdivinar and intentos!=0:
    print(numAdivinar)
    print("Te quedan",intentos," intentos restantes")
    numInput=int(input("Escriba un numero: "))
    if numInput!=numAdivinar:
        intentos-=1
        print("El numero",numInput," no ha sido correcto")

if numInput!=numAdivinar:
    print("Te has quedado sin intentos, el numero era", numAdivinar)
else:
    print("Enhorabuena, el numero", numInput," es correcto")