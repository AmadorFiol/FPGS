#Crear una lista de las combinaciones de 2 números del 1 al 10  (utilizando itertools.combinations)
#Crear una lista de las combinaciones de 3 números del 1 al 10  (utilizando itertools.combinations)
import itertools
array=[num for num in itertools.combinations(range(0,11),2)]
print("Combinaciones disponibles de 2 numeros\n",array)
array=[num for num in itertools.combinations(range(0,11),3)]
print("Combinaciones disponibles de 3 numeros\n",array)