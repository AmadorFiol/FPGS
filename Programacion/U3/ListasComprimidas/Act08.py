#Crear una lista de los números primos del 1 al 100.
#Crea una lista con los 100 primeros números primos.
def check_primo(numero):
    for i in range(2,numero):
        if numero%i==0:
            return False
    return True

primos=[num+1 for num in range(0,100) if check_primo(num+1)]
print("Numeros primos entre 1 y 100\n",primos)

primos=[num+1 for num in range(0,525) if check_primo(num+1)]
print("Los 100 primeros numeros primos son\n",primos)