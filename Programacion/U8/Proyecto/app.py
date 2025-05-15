import os
from datetime import datetime
#-----Variables Y Constantes-----#
salir=False
SKIPFILES=["app.py","log.txt","users.txt"]
DIRS=["Backups","Contratos","Facturas","Informes"]
log=open("log.txt","a")


#-----Funciones-----#
def login():
    userIn=input("Escriba su nombre de usuario: ")
    passIn=input("Escriba su contraseña: ")
    file=open("users.txt","r")
    for line in file.readlines():
        line=line.split(",")
        if line[0]==userIn and line[1].replace("\n","")==passIn:
            print(f"Bienvenido {userIn}")
            file.close()
            return userIn
    print(f"Usuario o contraseña incorrecto")
    file.close()
    exit()

def move_file(ruta,file,log):
    os.system(f"move {file} {ruta}\\{file}")
    log.write(f"[{datetime.now()}] El archivo {file} se ha movido a {ruta}\n")
    print(f"El archivo {file} se ha movido a {ruta}")

def get_ruta(ext):
    match(ext):
        case "xls":
            return "Facturas"
        case "docx":
            return "Contratos"
        case "pdf":
            return "Informes"
        case "txt":
            return "Backups"
        case _:
            pass  

def org_files():
    
    dir=os.listdir(".\\")
    print(dir)
    #Este check es por si se ejecuta en el directorio equivocado no provocar lios
    decided=False
    while(not decided):
        match(input("Esta seguro de continuar (Y/N): ").upper()):
            case "Y" | "S":
                print("Se comenzara con la operacion")
                decided=True
            case "N":
                print("Cancelando operacion")
                decided=True
            case _:
                print("Opcion no valida, se considerara un no")
                os.system("pause")

    for file in dir:
        try:
            ruta=get_ruta(file.split(".")[1])
            if file in SKIPFILES:
                pass
            elif ruta not in dir:
                os.system(f"mkdir {ruta}")
                dir.append(ruta)
                log.write(f"[{datetime.now()}] Se ha creado la carpeta {ruta}\n")
                print(f"Se ha creado la carpeta {ruta}")
                move_file(ruta,file,log)
            else:
                if file in os.listdir(f".\\{ruta}"):
                    raise FileExistsError
                else:
                    move_file(ruta,file,log)
        except IndexError: #Este error salta cuando se encuentra una carpeta
            pass
        except FileExistsError:
            decided=False
            while(not decided):
                print(f"El archivo ya existe en la carpeta {ruta}")
                match(input("Quiere cambiar el archivo antiguo por el actual? (Y/N) ").upper()):
                    case "Y" | "S":
                        move_file(ruta,file,log)
                        decided=True
                    case "N":
                        print("Pasando al siguiente archivo")
                        decided=True
                    case _:
                        print("Esa no es una opcion valida")
                        os.system("pause")
        except PermissionError:
            print(f"No tienes lo permisos correspondientes para move_file {file}, se pasara al siguiente archivo")
    

def search_file(fileIn):
    try: #Hay extension de archivo
        for file in os.listdir(".\\"): #Posibilidad de comenzar a buscar sin haber organizado antes
            if fileIn==file:
                print(f"Hay una coincidencia en tu ruta actual ({file})")

        if fileIn.split(".")[1] is not None:
            ruta=get_ruta(fileIn.split(".")[1])
            if fileIn in os.listdir(ruta):
                print(f"Hay una coincidencia en la carpeta {ruta}")

    except IndexError: #No hay extension del archivo
        for file in os.listdir(".\\"): #Posibilidad de comenzar a buscar sin haber organizado antes
            if fileIn==file.split(".")[0]:
                print(f"Hay una coincidencia en tu ruta actual ({file})")

        for dir in DIRS:
            for file in os.listdir(dir):
                if fileIn==file.split(".")[0]:
                    print(f"Hay una coincidencia en la carpeta {dir}")
    
def do_backup(fileIn):
    
    try:
        if fileIn.split(".")[1] is not None:
            ruta=get_ruta(fileIn.split(".")[1])
            if ruta=="Backups":
                print("No se puede hacer un backup de un backup")
            elif fileIn in os.listdir(ruta):
                for file in os.listdir(ruta):
                    if fileIn==file:
                        if f"{fileIn.split(".")[0]}.txt" in os.listdir("Backups"):
                            raise FileExistsError
                        os.system(f"copy .\\{ruta}\\{fileIn} .\\Backups\\{fileIn.split(".")[0]}.txt")
                        log.write(f"[{datetime.now()}] Se ha realizado un backup de {file}\n")
                        print(f"Se ha realizado un backup de {file}")
            else:
                raise FileNotFoundError
            
    except IndexError:
        print("Escriba la extension del archivo tambien porfavor")
    except FileNotFoundError:
        print("El archivo no se ha encontrado\n Por favor, si no lo ha hecho ya primero seleccione la opcion de Reorganizar archivos")
    except FileExistsError:
        #Prodecer a preguntar si quiere cambiar el backup antiguo por el actual
        decided=False
        while(not decided):
            print(f"El archivo ya tiene un backup")
            match(input("Quiere cambiar el backup antiguo por el actual? (Y/N) ").upper()):
                case "Y" | "S":
                    os.system(f"copy .\\{ruta}\\{fileIn} .\\Backups\\{fileIn.split(".")[0]}.txt")
                    log.write(f"[{datetime.now()}] Se ha realizado un backup de {file}\n")
                    print(f"Se ha realizado un backup de {file}")
                    decided=True
                case "N":
                    print("Cancelando operacion")
                    decided=True
                case _:
                    print("Esa no es una opcion valida")
                    os.system("pause")

def restore_file(fileIn):
    pass
    '''
    Hacer lo mismo que con do_backup pero copiando del backup
    a la ruta del archivo a restaurar y cambiando ext del backup
    '''
    
#-----Main-----#
login()
while(not salir):
    print("Escoja una opcion")
    print("1. Reorganizar archivos")
    print("2. Buscar archivo")
    print("3. Realizar backup")
    print("S. Salir")
    match(input("Escriba la opcion deseada: ").upper()):
        case "1":
            org_files()
        case "2":
            search_file(input("Escriba el nombre del archivo: "))
        case "3":
            do_backup(input("Escriba el nombre del archivo con la extension: "))
        case "S":
            log.close()
            salir=True
        case _:
            print("Esa no es una opcion valida")
    os.system("pause")
    os.system("cls")