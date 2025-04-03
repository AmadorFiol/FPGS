'''
Crea una función llamada `imprimir_info` que acepte múltiples argumentos (*args)
y múltiples argumentos con nombre (**kwargs) para mostrar una lista de elementos
y sus detalles.
'''
def imprimir_info(*args,**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave}:{valor}")
    print("Otra informacion")
    for arg in args:
        print(arg)

imprimir_info("Palma","Hombre",nombre="Amador",edad=19)