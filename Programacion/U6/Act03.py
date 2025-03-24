'''
Escribe un programa que lea una cadena del usuario y luego intente convertirla a un número entero.
Si la cadena no se puede convertir a un número entero, imprime un mensaje de error.
'''
userInput=input("Escribe cualquier cosa: ")
try:
    userInput=int(userInput)
    print("El string puede ser trasnformada a un int")
except ValueError:
    print("No se puede transformar el string a un entero")