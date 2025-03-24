'''
Escribe un programa que intente llamar a una función que no existe.
Si la función no existe, captura la excepción y muestra un mensaje de error.
'''
# def funcion():
#     print("Soy una funcion")

try:
    funcion()
except NameError:
    print("404 Funcion no encontrada")