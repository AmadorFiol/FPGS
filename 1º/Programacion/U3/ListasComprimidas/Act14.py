#Crea un diccionario que contenga los cuadrados de los primeros 5 números enteros (empezando en 1) usando dict comprehension.
diccionario={clave+1:valor**2 for clave,valor in enumerate(range(1,11))}
print(diccionario)