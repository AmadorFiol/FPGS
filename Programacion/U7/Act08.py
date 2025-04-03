'''
Escribe una función llamada `maximo` que reciba un número
variable de valores numéricos (*args) y devuelva el mayor de ellos.
'''
def maximo(*args):
    max=args[0]
    for arg in args:
        if arg>max:
            max=arg
    return max

print(maximo(4,10,-1,300,23))