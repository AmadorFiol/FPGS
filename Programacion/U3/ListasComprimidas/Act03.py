#Crear una lista comprimida con  los primeros 10 números pares.
#Crear una lista comprimida con los números pares que hay entre 0 y 10.
pares=[num*2 for num in range(1,11)]
print("Primeros 10 pares:\n",pares)
pares=[numero for numero in range(1, 11) if numero % 2 == 0]
print("Pares entre el 1 al 10:\n",pares)