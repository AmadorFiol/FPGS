import datetime, os

def show_users():
    users={}
    with open("./accesos.log", "r") as file:
        for line in file.readlines():
            if line.split(" ")[1] in users:
                pass
            else:
                users.append(line.split(" ")[1])
    file.close()
    for user in users:
        print(user)

def show_users_and_timesLogged():
    users={}
    with open("./accesos.log", "r") as file:
        for line in file.readlines():
            if line.split(" ")[1] in users:
                users[line.split(" ")[1]]+=1
            else:
                users[line.split(" ")[1]]=1
    file.close()
    for user,timesLogged in users.items():
        print(f"{user} se ha entrado {timesLogged}")

def copy_file():
    newFile=input("Escribe el nombre del nuevo fichero? ")
    with open("./accesos.log","r") as file:
        data=file.read()
    file.close()
    with open(f"./{newFile}","w") as file:
        file.write(data)
        print("Archivos copiados correctamente")
    file.close()

name=input("Cual es tu nombre? ")
with open("./accesos.log","a") as file:
    file.write(f"Usuario {name} a las {datetime.datetime.now()} ha entrado\n")
file.close()

salir=False
while(salir==False):
    print("Escoja una opcion")
    print("1. Mostrar usuarios que han entrado")
    print("2. Mostrar usuarios y las veces que han entrado")
    print("3. Copiar archivo accesos.log a otro")

    print("S. Salir")

    match(input()):
        case "1":
            show_users()
        case "2":
            show_users_and_timesLogged()
        case "3":
            copy_file()
        case "S":
            salir=True
        case _:
            print("Escriba el numero de la opcion que quieres seleccionar")
    os.system("pause")
    os.system("cls")