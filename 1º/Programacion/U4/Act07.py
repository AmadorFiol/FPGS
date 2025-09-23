'''
En esta actividad, vamos a crear una clase en Python que represente un libro. La clase debe tener los siguientes atributos:
titulo: El título del libro.
autor: El autor del libro.
genero: El género del libro.
paginas: El número de páginas del libro.


Además, la clase debe tener los siguientes métodos:
init(self, titulo, autor, genero, paginas): El método constructor de la clase.
get_titulo(self): El método que devuelve el título del libro.
get_autor(self): El método que devuelve el autor del libro.
get_genero(self): El método que devuelve el género del libro.
get_paginas(self): El método que devuelve el número de páginas del libro.
set_titulo(self, titulo): El método que establece el título del libro.
set_autor(self, autor): El método que establece el autor del libro.
set_genero(self, genero): El método que establece el género del libro.
set_paginas(self, paginas): El método que establece el número de páginas del libro.
'''
import os
#-----Declaramos clases-----#
class Libro():
    def __init__(self,titulo,autor,genero,paginas):
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        self.paginas=paginas
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_genero(self):
        return self.genero
    def get_paginas(self):
        return self.paginas
    def set_titulo(self,titulo):
        self.titulo=titulo
    def set_autor(self,autor):
        self.autor=autor
    def set_genero(self,genero):
        self.genero=genero
    def set_paginas(self,paginas):
        self.paginas=paginas
#-----Declaramos variables-----#
salir=False
listadoLibros=[]

#-----Declaramos funciones-----#
def seleccionar_libro():
    libroSel=None
    while(libroSel==None):
        
        for num,libro in enumerate(listadoLibros):
            print(f"{num+1}. {libro.titulo} {libro.autor}")
        print("a. Añadir Producto")
        userInput=input("Que libro vas a pillar? ")
        userNum=0
        try:
            userNum=int(userInput)-1
        except:
            pass
        if(userNum not in range(0,len(listadoLibros)) and userInput!="a"):
            print("Esa opcion no esta en el listado")
        else:
            if userInput=="a":
                libroSel=add_libro()
            elif userNum in range(0,len(listadoLibros)):
                libroSel=listadoLibros[userInput-1]
            else:
                print("Escriba una opcion")
    return libroSel

def add_libro():
    titulo=input("Cual es el titulo del libro? ")
    autor=input("Cual es su autor? ")
    genero=input("Cual es el genero principal? ")
    paginas=input("Cuantas paginas tiene? ")

    listadoLibros.append(Libro(titulo,autor,genero,paginas))
    libroSel=listadoLibros[-1]
    return libroSel

#-----Main-----#
libroSel=seleccionar_libro()
os.system("cls")
while(salir==False):
    print("1. Mostrar titulo")
    print("2. Mostrar autor")
    print("3. Mostrar genero")
    print("4. Mostrar cantidad paginas")
    print("5. Cambiar titulo")
    print("6. Cambiar autor")
    print("7. Cambiar genero")
    print("8. Cambiar cantidad paginas")
    print("9. Seleccionar otro libro")
    print("10. Añadir libro")
    print("S. Salir")
    match(input("Que quieres hacer? ")):
        case "1":
            print(libroSel.get_titulo())
            os.system("pause")
        case "2":
            print(libroSel.get_autor())
            os.system("pause")
        case "3":
            print(libroSel.get_genero())
            os.system("pause")
        case "4":
            print(libroSel.get_paginas())
            os.system("pause")
        case "5":
            nuevoTitulo=input("Escribe el nuevo titulo del libro: ")
            libroSel.set_titulo(nuevoTitulo)
            os.system("pause")
        case "6":
            nuevoAutor=input("Escribe el nuevo autor del libro: ")
            libroSel.set_autor(nuevoAutor)
            os.system("pause")
        case "7":
            nuevoGenero=input("Escribe el nuevo genero del libro: ")
            libroSel.set_genero(nuevoGenero)
            os.system("pause")
        case "8":
            nuevoPaginas=input("Escribe el nuevo recuento de paginas: ")
            libroSel.set_paginas(nuevoPaginas)
            os.system("pause")
        case "9":
            libroSel=seleccionar_libro()
            os.system("pause")
        case "10":
            libroSel=add_libro()
            os.system("pause")
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")
            os.system("pause")
    os.system("cls")