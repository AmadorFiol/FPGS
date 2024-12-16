'''
Crear una lista de las sumas de los números del 1 al 10.
Crear una lista de las restas de los números del 1 al 10.
Crear una lista de los multiplicación de los números del 1 al 10.
Crear una lista de las divisiones de los números del 11 al 10.
'''

def calculo(numInicial,accion):
    resultado=0
    match(accion):
        case "s":
            for num in range(numInicial,11):
                resultado=resultado+num
        case "r":
            for num in range(numInicial,11):
                resultado=resultado-num
        case "m":
            resultado=1
            for num in range(numInicial,11):
                resultado=resultado*num
        case "d":
            resultado=1
            for num in range(numInicial,11):
                resultado=resultado/num
    return resultado

array=[calculo(num,"s") for num in range(1,11)]
print("Las sumas:\n",array)

array=[calculo(num,"r") for num in range(1,11)]
print("Las restas:\n",array)

array=[calculo(num,"m") for num in range(1,11)]
print("Las multiplicaciones:\n",array)

array=[calculo(num,"d") for num in range(1,11)]
print("Las divisiones:\n",array)
