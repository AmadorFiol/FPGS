'''
Crear una clase en Python que represente un Producto.
Los atributos de un producto serán su nombre, su precio y su descripción. Los métodos de la clase serán los siguientes:
__init__(): Crea un nuevo producto con los atributos especificados.
get_nombre(): Devuelve el nombre del producto.
get_precio(): Devuelve el precio del producto.
get_descripcion(): Devuelve la descripción del producto.
set_nombre(): Modifica el nombre del producto.
set_precio(): Modifica el precio del producto.
set_descripcion(): Modifica la descripción del producto.
'''
import os
#-----Declaramos clases-----#
class Producto():
    def __init__(self,nombre,precio,descripcion):
        self.nombre=nombre
        self.precio=precio
        self.descripcion=descripcion
    
    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def get_descripcion(self):
        return self.descripcion

    def set_nombre(self,nombre):
        self.nombre=nombre
    
    def set_precio(self,precio):
        self.precio=precio

    def set_descripcion(self,descripcion):
        self.descripcion=descripcion

#-----Declaramos variables-----#
listadoProductos=[
    Producto("Guantes",10,"Caja de 25 guantes"),
    Producto("Esponjas",6,"Pack de 2 esponjas"),
    Producto("Pringles",3.99,"Una lata de pringles")
]
salir=False

#-----Declaramos funciones-----#
def seleccionar_producto():
    productoSel=None
    while(productoSel==None):
        for num,producto in enumerate(listadoProductos):
            print(f"{num+1}. {producto.nombre} {producto.precio}€")
        userInput=int(input("Que producto vas a pillar? "))
        if(userInput-1 not in range(0,len(listadoProductos))):
            print("Esa opcion no esta en el listado")
        else:
            productoSel=listadoProductos[userInput-1]
            return productoSel

def add_producto():
    nombre=input("Cual es el nombre del producto? ")
    precio=input("Cual es su precio? ")
    descripcion=input("Haz una breve descripcion del producto: ")

    listadoProductos.append(Producto(nombre,precio,descripcion))
    productoSel=listadoProductos[-1]
    return productoSel

#-----Main-----#
productoSel=seleccionar_producto()
os.system("cls")
while(salir==False):
    print("1. Mostrar nombre")
    print("2. Mostrar precio")
    print("3. Mostrar descripcion")
    print("4. Cambiar nombre")
    print("5. Cambiar precio")
    print("6. Cambiar descripcion")
    print("7. Seleccionar otro producto")
    print("8. Añadir producto")
    print("S. Salir")
    match(input("Que quieres hacer? ")):
        case "1":
            print(productoSel.get_nombre())
            os.system("pause")
        case "2":
            print(productoSel.get_precio())
            os.system("pause")
        case "3":
            print(productoSel.get_descripcion())
            os.system("pause") 
        case "4":
            nuevoNombre=input("Escribe el nuevo nombre del producto: ")
            productoSel.set_nombre(nuevoNombre)
            os.system("pause")
        case "5":
            nuevoPrecio=input("Escribe el nuevo precio del producto: ")
            productoSel.set_precio(nuevoPrecio)
            os.system("pause")
        case "6":
            nuevoDescripcion=input("Escribe el nuevo Descripcion del producto: ")
            productoSel.set_descripcion(nuevoDescripcion)
            os.system("pause")
        case "7":
            productoSel=seleccionar_producto()
            os.system("pause")
        case "8":
            productoSel=add_producto()
            os.system("pause")
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")
            os.system("pause")
    os.system("cls")