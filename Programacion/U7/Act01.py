'''
Escribe una función llamada multiplicar_numeros que acepte una cantidad
variable de números y devuelva la multiplicacion de todos ellos
'''
def multiplicacion(*numeros):
    var=1
    for num in numeros:
        var*=num
    return var

multiplicacion(1,2,3,4,5)