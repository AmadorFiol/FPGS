'''
Escribe un programa que intente abrir un archivo.
Si el archivo no existe, imprime un mensaje de error.
'''
try:
    with open("./test.txt") as file:
        for line in file:
            print(line)
    file.close()
except FileNotFoundError:
    print("404 Archivo no encontrado")