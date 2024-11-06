def negativo(num):
    if(num>0):
        print("El numero negativo de",num," es:",num*-1)
    elif(num==0):
        print("El numero 0 no tiene negativo")
    else:
        print("El numero proporcionado ya es negativo")

num=int(input("Dime un numero: "))
negativo(num)