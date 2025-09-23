'''
Desarrolla una función llamada encontrar_minimo que reciba
una cantidad variable de números y devuelva el mínimo de ellos.
'''
def encontrar_minimo(*args):
    #print(min(args))
    minimo=args[0]
    for arg in args:
        if minimo>arg:
            minimo=arg
    print(minimo)
    
encontrar_minimo(4,-1,2,0,-7)