'''
Escribe un programa que lea un número entero del usuario y luego intente dividirlo
por otro número entero. Si el segundo número es cero, imprime un mensaje de error.
'''
num=input("Escribe un numero: ")
try:
    num=int(num)
    result=10/num
    print(f"El resultado es {result}")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except:
    print(f"{num} no es un numero")