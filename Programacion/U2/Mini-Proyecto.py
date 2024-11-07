import random,os,time

bbdd_dados=[]
salir=False

def trhow_dados():
    dados=(random.randint(1,6),random.randint(1,6))
    bbdd_dados.append(dados)
    show_dados(dados)

def show_dados(dados):
    print("*****   *****")
    print("*",dados[0],"*   *",dados[1],"*")
    print("*****   *****")
    time.sleep(2)

def show_media():
    sum=0
    div=0
    for tuplas in bbdd_dados:
        for i in tuplas:
            sum=sum+i
            div+=1
    media=sum/div
    print("De",div,"tiradas, la media es:",media)
    time.sleep(3)

def show_estadisticas():
    cantDados=[0,0,0,0,0,0]
    for tuplas in bbdd_dados:
        for i in tuplas:
            cantDados[i-1]+=1
        
    for i in range(1,len(cantDados)+1):
        print("El numero", i," ha salido:",cantDados[i-1])
    time.sleep(3)


while(salir==False):
    os.system('cls')
    print("Bienvenido al casino")
    print("T. Tirar unos dados")
    print("M. Media aritmetica")
    print("E. Estadisticas de tiradas")
    print("V. Ver ultima tirada")
    print("S. Salir")

    match(input()):
        case "T":
            trhow_dados()

        case "M":
            show_media()
        case "E":
            show_estadisticas()
        case "V":
            show_dados(bbdd_dados[-1])
        case "S":
            salir=True
        case _:
            print("Esa opción no es correcta, vuelva a intentarlo")
            time.sleep(2)