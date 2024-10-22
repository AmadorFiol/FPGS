#Crear script que pida un numero, si es un numero par y su doble esta entre 10 y -10 enviar mensaje "OK"
num=int(input("Dime un numero (puede ser negativo): "))
if(num*2>=-10 and num*2 <=10 and num%2==0):
    print("OK")