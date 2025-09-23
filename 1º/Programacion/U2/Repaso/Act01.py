import os
salir=False
tareasArray=[]

def check_existe(nomTarea):
    for tarea in tareasArray:
        if nomTarea==tarea["nombre"]:
            return True

def check_estado(nomTarea):
    for tarea in tareasArray:
        if nomTarea==tarea["nombre"] and tarea["completada"]==False:
            return True

def check_tareasPendientes():
    for tarea in tareasArray:
        if check_estado(tarea["nombre"])==True:
            return True

def add_tarea():
    nomTarea=input("Inserte el nombre de la tarea (o \"C\" para cancelar) ").upper()
    if nomTarea=="C":
        return
    if check_existe(nomTarea)!=True:
        tareasArray.append({"nombre":nomTarea,"completada":False})
        print("Se ha creado la tarea")
    else:
        print("Ya existe una tarea con ese nombre")
    os.system("pause")

def show_tarea():
    for num,tarea in enumerate(tareasArray):
        if tarea["completada"]==False:
            print(f"{num+1}-{tarea["nombre"]}. Aun por completar")
        else:
            print(f"{num+1}-{tarea["nombre"]}. Completada")
    if check_tareasPendientes()!=True:
        print("\nYa no quedan tareas pendientes")
    os.system("pause")

def change_estado():
    nomTarea=input("Escriba el nombre de la tarea (o \"C\" para cancelar) ").upper()
    if nomTarea=="C":
        return
    for tarea in tareasArray:
        if nomTarea==tarea["nombre"] and tarea["completada"]==False:
            tarea["completada"]=True
            print("Se ha marcado la tarea como completada")
        elif nomTarea==tarea["nombre"] and tarea["completada"]==True:
            print("La tarea ya esta completada")
    if check_tareasPendientes()!=True:
                print("\nYa no quedan tareas pendientes")
    os.system("pause")

def del_tarea():
    nomTarea=input("Escriba el nombre de la tarea (o \"C\" para cancelar) ").upper()
    if nomTarea=="C":
        return
    for tarea in tareasArray:
        if nomTarea==tarea["nombre"] and tarea["completada"]==False:
            tareasArray.remove(tarea)
            print("Se ha eliminado la tarea")
        elif nomTarea==tarea["nombre"] and tarea["completada"]==True:
            print("No se puede eliminar una tarea completada")
    if check_tareasPendientes()!=True:
        print("\nYa no quedan tareas pendientes")

while(salir==False):
    os.system("cls")
    if check_tareasPendientes()==True:
        print("Que quieres hacer?")
        print("1. Agregar Tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        match(input()):
            case "1":
                add_tarea()
            case "2":
                show_tarea()
            case "3":
                change_estado()
            case "4":
                del_tarea()
            case "5":
                salir=True
                print("Adios")
            case _:
                print("Esa no es una opcion valida")
                os.system("pause")
    else:
        print("Que quieres hacer?")
        print("1. Agregar Tarea")
        print("2. Listar tareas")
        print("3. Salir")

        match(input()):
            case "1":
                add_tarea()
            case "2":
                show_tarea()
            case "3":
                salir=True
                print("Adios")
            case _:
                print("Esa no es una opcion valida")
                os.system("pause")