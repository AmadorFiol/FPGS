'''
Define un valor de inicio y calcula el cuadrado de los “n” siguientes valores.
Estos dos parámetros los deberá introducir el usuario por consola. Hazlo mediante diccionarios comprimidos.
Por ejemplo si inicio=5 y n=3, deberá mostrarse {6: 36, 7: 49, 8: 64}.
'''
inicio=int(input("Escriba un valor inicial "))
nums=int(input("Cuantos numeros quieres elevar al cuadrado? "))

diccionario={clave:valor**2 for clave,valor in enumerate(range(inicio,(inicio+nums)),inicio)}
print(diccionario)