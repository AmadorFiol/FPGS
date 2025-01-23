'''
Construye una clase llamada Tienda en Python que mantenga un inventario global de productos.
Cada vez que se añade un nuevo producto al inventario, el contador total de productos en la tienda debe incrementarse.
Utiliza métodos y atributos estáticos para implementar esta funcionalidad.

La clase debe tener los siguientes elementos:
Un atributo estático llamado total_productos que representa el contador global de productos en la tienda.
Un método estático llamado agregar_producto() que incrementa el contador de productos cada vez que se llama 
y muestra un mensaje indicando que se ha agregado un producto al inventario.Un método estático llamado obtener_total_productos()
que devuelve el total de productos en la tienda.

Crea instancias de la clase y utiliza los métodos estáticos para agregar productos al inventario y 
obtener el total de productos en la tienda.
'''
import os
#-----Declaramos clases-----#
class Tienda():
    def __init__(self):
        self.totalProd=0

    def agregar_producto(self):
        self.totalProd+=1

    def get_totalProd(self):
        return self.totalProd

#-----Declaramos variables-----#
inv=Tienda()
salir=False
#-----Main-----#
while(salir==False):
    os.system("cls")
    print("Que quieres hacer? ")
    print("1. Agregar objeto al inventario")
    print("2. Mirar el total de productos")
    print("S. Salir")
    match(input("")):
        case "1":
            inv.agregar_producto()
            print("Se ha agregado un objeto al inventario")
        case "2":
            print(f"Cantidad de objetos actual: {inv.get_totalProd()}")
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")
    if salir==False:
        os.system("pause")

