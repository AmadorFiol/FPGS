import random
libro=[]
salir=False

def crear_poesia(estrofas, versos):
    poesia=[]
    for estrofa in range(0,estrofas):
        versosArray=[]
        for verso in range(0,versos):
            versosArray.append(verso+1)
        poesia.append(versosArray)
    return poesia

def crear_libro(nombre,num_poesias):
    for poesia in range(0,num_poesias+1):
        estrofas=random.randint(1,5)
        versos=random.randint(1,5)
        print("La poesia",poesia+1,"tendra",estrofas,"estrofas y",versos,"versos")
        libro.append(crear_poesia(estrofas,versos))

def mostrar_libro():
    for num,poesias in enumerate(libro):
        print("La poesia",num,"es")
        for estrofa in poesias:
            for verso in estrofa:
                print(verso,end=" ")
            print("\n")

while(salir==False):
    print("1. Crear nuevo libro")
    print("2. Mostrar libros")
    print("S. Salir")
    
    match(input("")):
        case "1":
            num_poesias=int(input("Y cuantas poesias? "))
            crear_libro(nombre="",num_poesias=int(1))
        case "2":
            mostrar_libro()
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")