'''
Escribe un programa que pida al usuario el nombre de un archivo de origen y el de destino,
y copie el contenido del primero al segundo. Maneja las siguientes excepciones:
    El archivo de origen no existe.
    El archivo de destino no tiene permisos de escritura.
    El archivo de origen está vacío.
'''
class FileIsEmpty(Exception):
    def __init__(self, file, message="Archivo vacio"):
        self.file = file
        super().__init__(f"{message}:{file}")
    
    def check_file_not_empty(file):
        if not file.read().strip():
            raise FileIsEmpty(file)
        else:
            return

try:
    with open("./test.txt","r") as fileOrigin, open("./testDestino","w") as fileDestiny:
        FileIsEmpty.check_file_not_empty(fileOrigin)
        for line in fileOrigin:
            fileDestiny.write(line)
    fileDestiny.close()
    fileOrigin.close()

except FileNotFoundError:
    print("404 Archivo no encontrado")
except IOError:
    print("Error de permisos no validos")
except FileIsEmpty:
    print("Archivo origen vacio")
