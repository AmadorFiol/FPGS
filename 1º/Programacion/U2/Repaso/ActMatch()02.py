import os
salir=False
frase=""

def create_frase(frase):
    if frase=="":
        print("Escriba una frase")
        frase=input()
    return(frase)

def conteo_palabras():
    fraseArray=frase.split()
    print("La frase \'",frase,"\' tiene",len(fraseArray),"palabras")
    os.system("pause")

def show_mayus():
    fraseMayus=frase.upper()
    print(fraseMayus)
    os.system("pause")

while(salir==False):
    os.system("cls")
    frase=create_frase(frase)
    os.system("cls")
    print("Frase:",frase)
    print("Que deseas hacer")
    print("1. Numero palabras")
    print("2. Transformar todo a mayusculas")
    print("3. Cambiar frase")
    print("S. Salir")

    match(input()):
        case "1":
            conteo_palabras()
        case "2":
            show_mayus()
        case "3":
            frase=""
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")
            os.system("pause")