'''
Crear una lista de los números del 1 al 100 que sean divisibles por 3.
Crear una lista de los números del 1 al 100 que sean divisibles por 5.
'''
div=int(input("Cual sera el divisor? "))
array=[num for num in range (1,101) if num%div==0]
print(array)