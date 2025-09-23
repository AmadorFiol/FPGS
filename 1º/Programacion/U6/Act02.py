'''
Escribe un programa que lea un número entero del usuario y luego intente dividirlo
por otro número entero. Si el segundo número es cero, imprime un mensaje de error.
'''
dividendo=input("Escribe el dividendo: ")
divisor=input("Escribe el divisor: ")
try:
    dividendo=int(dividendo)
    divisor=int(divisor)
    result=dividendo/divisor
    print(f"El resultado es {result}")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except ValueError:
    print(f"Alguno de los valores no es un numero")