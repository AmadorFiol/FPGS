import os,random
#----------Inicialización de variables----------#
salir=False #Variable de control del bucle main

#Diccionario en el que se almacena las opciones del menu
menu={
    1:"Añadir nombre",
      2:"Añadir verbo",
      3:"Añadir adjetivo",
      4:"Mostrar nombre",
      5:"Mostrar verbos",
      6:"Mostrar adjetivos",
      7:"Crear una frase",
      8:"Crear una cancion",
      9:"Crear un disco",
      10:"Mostrar la discografia",
      11:"Mostrar un disco",
      "S":"Salir"
      }

#Array en los que se almacenan sus respectivos valores
nombres=[
    "Jose",
    "Pepe",
    "Amador",
    "Ana",
    "Ines"
]
verbos=[
    "corre",
    "canta",
    "llora",
    "baila",
    "salta"
]
adjetivos=[
    "alto",
    "bajo",
    "feliz",
    "triste",
    "solo"
]
#Diccionario que sera usado para almacenar los discos guardados
discografia={}

#----------Funciones de inserción----------#
def insertarN(nombre):
    nombres.append(nombre)

def insertarV(verbo):
    verbos.append(verbo)

def insertarA(adjetivo):
    adjetivos.append(adjetivo)

#----------Funciones de mostrado----------#
'''
    Todas estas funciones hacen basicamente lo mismo
    recorren una variable en concreto (array o diccionario)
    y muestran su informacion
'''
def mostrarN():
    for nombre in nombres:
        print(nombre)

def mostrarV():
    for verbo in verbos:
        print(verbo)

def mostrarA():
    for adjetivo in adjetivos:
        print(adjetivo)

'''
    Como extra decidi que esta tuviera tambien una numeracion
    porque senti que asi se veria mejor
'''
def mostrar_discografia():
    for num,cd in enumerate(discografia):
        print(num+1,".",cd)

'''
    Funcion que muestra las canciones de un disco en especifico
'''
def mostrar_cd(nombre):
    for cancion in discografia[nombre]:
        print(cancion)

#----------Funciones de creación----------#
'''
    Con un randint selecciono los valores que conformaran la frase
    luego los concateno y guardo en una variable la cual tras ser
    devuleta sera 'printeada'
'''
def crear_frase():
    nombreElegido=nombres[random.randint(0,len(nombres)-1)]
    verboElegido=verbos[random.randint(0,len(verbos)-1)]
    adjetivoElegido=adjetivos[random.randint(0,len(adjetivos)-1)]
    frase=nombreElegido+" "+verboElegido+" "+adjetivoElegido
    return frase

'''
    Aqui lo que hago es anidar un bucle, por cada estrofa hay x versos
    cada verso concateno la cancion generada hasta el momento junto 
    a la frase generada con la llamada a crear_frase() y un salto de linea
    al final, luego una vez hechos los versos de esa estrofa vuelvo a
    concatenar un salto de linea para finalmente cuando devuelva
    la cancion este escrita de una manera ordenada
'''
def crear_cancion(estrofas,versos):
    cancion=""
    for estrofa in range(0,estrofas):
        for verso in range(0,versos):
            cancion=cancion+crear_frase()+"\n"
        cancion=cancion+"\n"
    return cancion

'''
    En esta funcion lo que hago es basicamente llamar a la funcion
    de crear_cancion la cantidad de veces requerida por el usuario
    y luego hago un .append para agregarla al array del cd el cual
    es luego finalmente añadido al diccionario "discografia" con la
    clave siendo el nombre indicado por el usuario
'''
def crear_cd(nombre,num_canciones):
    cd=[]
    for cancion in range(0,num_canciones):
        estrofas=int(input(f"Cuantas estrofas tendra la cancion numero {cancion+1}? "))
        versos=int(input("Y cuantos versos? "))
        newCancion=crear_cancion(estrofas,versos)
        print("La cancion numero",cancion+1,"es\n",newCancion)
        cd.append(newCancion)
    discografia[nombre]=cd

#----------Menu----------#
while(salir==False):
    os.system("cls")
    #Recorro el diccionario menu y muestro las opciones aprovechando
    #la clave como indicador de que escribir para seleccionar dicha opcion
    for opcion in menu:
        print(opcion,".",menu[opcion])
    
    match(input("Que quieres hacer? ")):
        case "1":
            insertarN(input("Escribe el nombre que quieres insertar "))
        case "2":
            insertarV(input("Escribe el verbo que quieres insertar "))
        case "3":
            insertarA(input("Escribe el adjetivo que quieres insertar "))
        case "4":
            mostrarN()
        case "5":
            mostrarV()
        case "6":
            mostrarA()
        case "7":
            os.system("cls")
            print("La frase creada es",crear_frase())
        case "8":
            os.system("cls")
            estrofas=int(input("Cuantas estrofas tendra la cancion "))
            versos=int(input("Y cuantos versos? "))
            print("La cancion creada es\n",crear_cancion(estrofas,versos))
        case "9":
            os.system("cls")
            nombre=input("Cual es el nombre del cd? ")
            num_canciones=int(input("Cuantas canciones tendra el cd? "))
            crear_cd(nombre,num_canciones)
        case "10":
            mostrar_discografia()
        case "11":
            mostrar_cd(input("Cual es el nombre del cd que quieres ver? "))
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")
    
    os.system("pause")