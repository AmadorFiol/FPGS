import os
salir=False
numero=0

def check_num(num):
    while(num<=0):
        if num<=0:
            num=int(input("Escriba un numero "))
            print("El numero ha de ser mayor a 0")
    return num

def check_primo():
    primo=True
    for i in range(2,numero):
        if numero%i==0:
            primo=False
            break
    if primo==True:
        print("Es primo")
    else:
        print("El numero no es primo")
    os.system("pause")

def show_factorial():
    factorial=numero
    for i in range(1,numero):
        factorial=factorial*i
    print("El factorial de",numero," es",factorial)
    os.system("pause")

while(salir==False):
    numero=check_num(numero)
    os.system("cls")
    print("El numero actual es",numero)
    print("Que desea realizar?")
    print("1. Comprobar si es numero primo")
    print("2. Realizar factorial")
    print("3. Cambiar el numero")
    print("S. Salir")
    
    match(input()):
        case "1":
            check_primo()
        case "2":
            show_factorial()
        case "3":
            numero=0
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")
            os.system("pause")