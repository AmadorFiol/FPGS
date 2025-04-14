import os
#-----Declaramos funciones-----#
def set_nota():
    nota=""
    while(nota is not int):
        nota=input("Escriba la nota (redondeada): ")
        try:
            nota=int(nota)
            return nota
        except:
            print("El valor introducido no es un numero entero")
            os.system("pause")
            os.system("cls")

def add_nota():
    try:
        with open("./notas.csv","a") as file:
            alumno=input("Escriba el nombre del alumno: ")
            asignatura=input("Escriba el nombre de la asignatura: ")
            nota=set_nota()
            file.write(f"{alumno},{asignatura},{nota}\n")
        file.close()
    except FileNotFoundError:
        print("El archivo objetivo no existe")
        return
    
def calc_media():
    sum=0
    i=0
    with open("./notas.csv","r") as file:
        for line in file.readlines():
            if line.split(",")[2]!="Nota":
                sum+=line.split(",")[2]
                i+=1
    file.close()
    print(sum/i)
    
def get_alumno(alumno):
    with open("./notas.csv","r") as file:
        for line in file.readlines():
            if line.split(",")[0]==alumno:
                return True      
    file.close()
    return False
def show_nota_alumno(alumno):
    pass

#-----Main-----#
salir=False
while(not salir):
    print("Escoja una opcion")
    print("1. Insertar nueva nota")
    print("2. Calcular media globlal")
    print("3. Mostrar notas de un alumno")
    print("4. ")

    print("S. Salir")

    match(input()):
        case "1":
            add_nota()
        case "2":
            calc_media()
        case "3":
            show_nota_alumno()
        case "S":
            salir=True
        case _:
            print("Escriba el numero de la opcion que quieres seleccionar")
    os.system("pause")
    os.system("cls")