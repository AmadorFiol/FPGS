'''
Escribe un programa que intente abrir un archivo en modo de escritura, pero el archivo ya está abierto en modo de lectura.
Si el archivo ya está abierto, captura la excepción y muestra un mensaje de error.
'''
try:
    with open("./test.txt","r") as file:
        with open("/test.txt","w") as file:
            pass

except FileNotFoundError:
    print("404 Archivo no encontrado")
except OSError:
    print("El archivo ya esta abierto")
    file.close()