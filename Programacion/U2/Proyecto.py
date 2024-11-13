import os

libro1={"nombre":"Dragon Ball","autor":"Akira Toriyama","disponibilidad":True}
libro2={"nombre":"Jujutsu Kaisen","autor":"Gege Akutami","disponibilidad":True}
libro3={"nombre":"Naruto","autor":"Masashi Kishimoto","disponibilidad":True}
libro4={"nombre":"One Piece","autor":"Eichiro Oda","disponibilidad":True}
libro5={"nombre":"ReZero","autor":"Tappei Nagatsuki","disponibilidad":False}
libros={1:libro1,2:libro2,3:libro3,4:libro4,5:libro5}
salir=False

def check_existe(titulo):
    for i in libros:
        if libros[i]["nombre"]==titulo:
            #Aprovecho el return para que cuando encuentre una coincidencia no continue con el bucle
            return True
        
def check_disponibilidad(titulo):
    for i in libros:
        if libros[i]["nombre"]==titulo and libros[i]["disponibilidad"]==True:
            return True
        elif libros[i]["nombre"]==titulo and libros[i]["disponibilidad"]==False:
            return False

def show_catalogo():
    for i in libros:
        print(i,".",libros[i]["nombre"]," de",libros[i]["autor"])
    os.system("pause")

def show_disponibilidad():
    libroUser=input("Inserte el titulo del libro ")
    if check_disponibilidad(libroUser)==True:
        print("El libro",libroUser," esta disponible")
    elif check_existe(libroUser)==True:
        print("El libro", libroUser," no esta disponible")
    else:    
        print("El libro", libroUser,"no se encuentra en el catalogo")  
        
    os.system("pause")

#He aprovechado esta funcion para poder realizar 2 funciones a la vez dependiendo de que quiera el usuario
#para asi no tener 2 funciones con el mismo funcionamiento exacto
def change_disponibilidad(accion):
    libroUser=input("Inserte el titulo del libro ")
    #Aqui uso variables para guardar el resultado de las funciones para no llamarlas varias veces
    #pero poder usar su resultado en multiples ocasiones
    disponibilidad=check_disponibilidad(libroUser)
    existe=check_existe(libroUser)
    if disponibilidad==accion:
        if input("Escriba 'C' y presione enter para confirmar ").upper()=="C":
            for i in libros:
                if libros[i]["nombre"]==libroUser:
                    #Segun la accion mostrar un mensaje u otro y cambiar la disponibilidad a la correspondiente
                    if accion==True:
                        libros[i]["disponibilidad"]=False
                        print("Reserva realizada con exito")
                    else:
                        libros[i]["disponibilidad"]=True
                        print("Devolucion realizada con exito")
        else:
            #Segun la accion mostrar un mensaje u otro
            if accion==True:
                print("Se ha cancelado la reserva, se te devolvera al menu")
            else:
                print("Se ha cancelado la devolucion, se te devolvera al menu")
    elif disponibilidad!=accion:
        if accion==True and existe==True:
            print("El libro", libroUser," no esta dispobible")
        elif accion==False and existe==True:
            print("El libro", libroUser," ya esta en la biblioteca")
        else:    
            print("El libro", libroUser,"no se encuentra en el catalogo") 
    os.system("pause")

def create_libro():
    nombreUser=input("Escribe el titulo ")
    autorUser=input("Escribe el nombre del autor ")
    libroUser={"nombre":nombreUser,"autor":autorUser,"disponibilidad":True}
    if input("Escriba 'C' y presione enter para confirmar ").upper()=="C":
        if check_existe(nombreUser)!=True:
            return libroUser
        else:
            print("El libro ya existe")
    else:
        print("Se ha cancelado la accion")
    os.system("pause")

def add_libro():
    libroAdd=create_libro()
    if libroAdd!="":
        #Explicacion de "globals()[f'libro{len(libros)+1}']". Crea una variable global con un nombre concatenando "libro"+(len(libros)+1)
        globals()[f'libro{len(libros)+1}']=libroAdd
        libros[len(libros)+1]=globals()[f'libro{len(libros)+1}']

while(salir==False):
    os.system("cls")
    print("Bienvenido a la Biblioteca de Amador")
    print("V. Ver catalogo")
    print("C. Consultar disponibilidad")
    print("R. Reservar libro")
    print("D. Devolver libro")
    print("I. Introducir libro")
    print("S. Salir")

    match(input("Que quieres hacer? ").upper()):
        case "V":
            show_catalogo()
        case "C":
            show_disponibilidad()
        case "R":
            change_disponibilidad(True)
        case "D":
            change_disponibilidad(False)
        case "I":
            add_libro()
        case "S":
            salir=True
            print("Adios")
        case _:
            print("Esa no es una opcion valida")
            os.system("pause")