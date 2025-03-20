'''
Escribe un programa que intente acceder a un elemento de una lista que no existe.
Si el elemento no existe, captura la excepción y muestra un mensaje de error.
'''
lista=["a","b"]
#lista.append("c")
try:
    print(lista[2])
except:
    print("404 Elemento no encontrado")