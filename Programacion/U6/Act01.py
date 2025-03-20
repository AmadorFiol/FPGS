'''
Escribe un programa que lea un número entero del usuario y luego imprima un mensaje indicando 
si el número es positivo, negativo o cero.
Si el usuario introduce un valor incorrecto (por ejemplo una palabra) dará un mensaje de error.
'''
num=input("Escribe un numero ")
try:
    num=int(num)
    if num<0:
        print(f"El numero {num} es negativo")
    elif num>0:
        print(f"El numero {num} es positivo")
    else:
        print("El numero introducido es un 0")
except:
    print("Eso no es un numero")