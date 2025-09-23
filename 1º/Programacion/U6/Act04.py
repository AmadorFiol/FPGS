'''
Escribe un programa que lea una lista de números enteros
del usuario y luego intente calcular la suma de los números.
Si la lista está vacía, imprime un mensaje de error.
'''
nums=[]
i=input("Cuantos numeros quieres escribir? ")
try:
    i=int(i)
except ValueError:
    print(f"{i} no es un valor numerico")
    exit()

for num in range(i):
        nums.append(input("Escribe un numero: "))

try:
    sum=0
    for num in nums:
        num=int(num)
        sum+=num
    print(f"La suma de esos numeros es {sum}")
except ValueError:
     print("Alguno de los valores no es un numero")