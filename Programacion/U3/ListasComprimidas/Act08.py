#Crear una lista de los números primos del 1 al 100.
#Crea una lista con los 100 primeros números primos.
primos=[]
print("Numeros primos entre 1 y 100\n",primos)
primo=True
for i in range(2,num):
    if num%i==0:
            primo=False
            break
    if primo==True:
        print("Es primo")
    else:
        print("El numero no es primo")