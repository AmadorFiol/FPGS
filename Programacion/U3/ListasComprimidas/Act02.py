#Crear una lista comprimida con los cuadrados de los números del 1 al 10.
#Crear una lista comprimida con los cubos de los números del 1 al 10.
cuadrados=[(num+1)**2 for num in range(0,10)]
cubos=[(num+1)**3 for num in range(0,10)]
print("Cuadrados:\n",cuadrados,"\nCubos\n",cubos)