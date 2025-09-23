import os

#Declaramos variables
libro1={"nombre":"Dragon Ball","autor":"Akira Toriyama","disponibilidad":True}
libro2={"nombre":"Jujutsu Kaisen","autor":"Gege Akutami","disponibilidad":True}
libro3={"nombre":"Naruto","autor":"Masashi Kishimoto","disponibilidad":True}
libro4={"nombre":"One Piece","autor":"Eichiro Oda","disponibilidad":True}
libro5={"nombre":"ReZero","autor":"Tappei Nagatsuki","disponibilidad":False}
libros={1:libro1,2:libro2,3:libro3,4:libro4,5:libro5}

salir=False #Variable de control del bucle del menu principal

#Declaramos funciones

'''
Funcion de busqueda en la que se busca una coincidencia entre el nombre del
libro que quiere el usuario y alguno de los libros de la biblioteca
'''
def check_existe(titulo):
    for i in libros:
        if libros[i]["nombre"].upper()==titulo.upper():
            #Aprovecho el return para que cuando encuentre una coincidencia no continue con el bucle
            return True

'''
Funcion de busqueda en la que se busca si el libro que quiere el usuario esta disponible
para ser reservado o no
'''     
def check_disponibilidad(titulo):
    for i in libros:
        if libros[i]["nombre"].upper()==titulo.upper() and libros[i]["disponibilidad"]==True:
            return True
        elif libros[i]["nombre"].upper()==titulo.upper() and libros[i]["disponibilidad"]==False:
            return False

'''
Funcion en la que recorro y muestro la informacion de todos
los libros a traves de un bucle
'''
def show_catalogo():
    for i in libros:
        print(i,".",libros[i]["nombre"]," de",libros[i]["autor"])
    os.system("pause")

'''
Funcion en la que muestro la disponibilidad de un libro
dependiendo la respuesta que me devuelva las funciones a las que llamo
muestro un mensaje u otro
'''
def show_disponibilidad():
    libroUser=input("Inserte el titulo del libro ")
    if check_disponibilidad(libroUser)==True:
        print("El libro",libroUser," esta disponible")
    elif check_existe(libroUser)==True:
        print("El libro", libroUser," no esta disponible")
    else:    
        print("El libro", libroUser,"no se encuentra en el catalogo, revise el nombre")  
        
    os.system("pause")

'''
Funcion en la que se realiza el cambio de disponibilidad de un libro
Dependiendo del parametro enviado sabe si la accion a realizar
es una reserva o una devolucion
'''
def change_disponibilidad(accion):
    libroUser=input("Inserte el titulo del libro ")
    '''
    Aqui uso variables para guardar el resultado de las funciones para no llamarlas varias veces
    pero poder usar su resultado en multiples ocasiones
    '''
    disponibilidad=check_disponibilidad(libroUser)
    existe=check_existe(libroUser)

    '''
    Si la disponibilidad corresponde con la necesaria para la accion que quiere usuario procede a entrar en un bucle
    en el que buscar el libro, sino no entra y directamente informa que no es posible relizar la accion deseada
    '''

    if disponibilidad==accion:
        if input("Escriba 'C' y presione enter para confirmar ").upper()=="C":
            for i in libros:
                if libros[i]["nombre"].upper()==libroUser.upper():
                    #Segun la accion mostrar un mensaje u otro y cambiar la disponibilidad a la correspondiente
                    if accion==True:
                        libros[i]["disponibilidad"]=False
                        print("Reserva realizada con exito")
                    else:
                        libros[i]["disponibilidad"]=True
                        print("Devolucion realizada con exito")
        else:
            #Segun la accion mostrar un mensaje u otro segun
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
            print("El libro", libroUser,"no se encuentra en el catalogo, revise el nombre") 
    os.system("pause")

'''
Funcion en la que se crea un libro con los datos del usuario
y si no hay coincidencias con alguno ya existente se procede llamar
a una funcion para añadir el libro al diccionario de libros
'''
def create_libro():
    nombreUser=input("Escribe el titulo ")
    autorUser=input("Escribe el nombre del autor ")
    libroUser={"nombre":nombreUser.title(),"autor":autorUser.title(),"disponibilidad":True}
    if input("Escriba 'C' y presione enter para confirmar ").upper()=="C":
        if check_existe(nombreUser)!=True:
            add_libro(libroUser)
        else:
            print("El libro ya existe")
    else:
        print("Se ha cancelado la accion")
    os.system("pause")

'''
Funcion que crea una variable dinamica y la añade al diccionario
de libros tambien generando una clave dinamicamente
'''
def add_libro(libroAdd):
    if libroAdd!="":
        '''
        Explicacion de "globals()[f'libro{len(libros)+1}']".
        Crear una variable global con un nombre dinamicamente concatenando "libro"+(len(libros)+1)
        '''
        globals()[f'libro{len(libros)+1}']=libroAdd
        libros[len(libros)+1]=globals()[f'libro{len(libros)+1}']
        print("El libro se ha anadido con exito")

#Programa principal
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
            create_libro()
        case "S":
            salir=True
            print("Adios")
        case _:
            print("Esa no es una opcion valida")
            os.system("pause")