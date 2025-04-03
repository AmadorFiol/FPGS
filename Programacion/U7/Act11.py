'''
Implementa una clase `Producto` que tenga un nombre, precio y cualquier número de características adicionales (**kwargs).
'''
class Producto():
    def __init__(self,nombre,precio,**kwargs):
        self.nombre=nombre
        self.precio=precio
        self.otraInfo=kwargs
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nPrecio: {self.precio}")
        for clave,valor in self.otraInfo.items():
            print(f"{clave}: {valor}")

prod=Producto("Patatillas",9.99,sabor="original",cantidad="500g")
prod.mostrar_info()