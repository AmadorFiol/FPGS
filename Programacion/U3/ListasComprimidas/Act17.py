'''
Diccionario comprimido que recorra del 1 al 5 pero solo guarde aquellos que su cuadrado es par
La clave sera el numero y el valor sera el cuadrado de ese numero
'''
diccionario={i:i**2 for i in range(1,6) if (i**2)%2==0}
print(diccionario)