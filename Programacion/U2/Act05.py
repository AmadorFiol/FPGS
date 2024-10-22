#Crear script que pida num y si esta entre 10 y -10 o su doble lo esta enviar mensaje "OK"
num=int(input("Dime un numero (puede ser negativo): "))
if(num*2>=-10 and num*2 <=10):
    print("OK")