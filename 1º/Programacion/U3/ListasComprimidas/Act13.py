'''
Crea una lista que recorra los números del 1 al 10
Si el valor es par aparece dicho valor,
si es impar aparece el booleano `False`.
'''
array=[num if num%2==0 else False for num in range(1,11)]
print(array)