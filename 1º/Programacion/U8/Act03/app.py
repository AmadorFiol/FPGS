import os
def mover(ext,file):
    os.system(f"move {file} {ext}/{file}")
    log.write(f"El archivo {file} se ha movido a {ext}\n")

def check_dir():
    dir=os.path.basename(os.getcwd())
    if dir != "Act03":
        notSecure=True
        while(notSecure):
            print(f"Estas ejecutando el programa en el directorio {dir}")
            match(input("Estas seguro de continuar (Y/N) ").upper()):
                case "Y" | "S":
                    notSecure=False
                case "N":
                    exit()
                case _:
                    print("Esa no es una opcion correcta, porfavor intente denuevo")
                    os.system("pause")
                    os.system("cls")
        os.system("cls")


log=open("log.txt","a")
check_dir()
dir=os.listdir("./")
print(dir)
for file in dir:
    try:
        ext=file.split(".")[1]
        if file=="app.py" or file=="log.txt":
            pass
        elif ext not in dir:
            os.system(f"mkdir {ext}")
            dir.append(ext)
            log.write(f"Se ha creado la carpeta {ext}\n")
            mover(ext,file)
        else:
            if file in os.listdir(f"./{ext}"):
                raise FileExistsError
            else:
                mover(ext,file)
    except IndexError: #Este error salta cuando se encuentra una carpeta
        pass
    except FileExistsError:
        print(f"El archivo ya existe en la carpeta {file.split(".")[1]}")
    except PermissionError:
        print("No tienes lo permisos correspondientes, se pasara al siguiente archivo")
log.close()
dir=os.listdir("./")
print(dir)