'''
Crea una función llamada descubrir que reciba una cantidad variable de argumentos
y te devuelva la cantidad exacta de números y la cantidad exacta de palabras.
'''
def intOrString(*args):
    numeros=0
    texto=0
    for arg in args:
        if arg is int or arg is float:
            numeros+=1
        else:
            texto+=1

    print(f"Hay un total de {len(args)} argumentos de los cuales {numeros} son numericos y {texto} son texto")


intOrString(1,2,"3","hola","10","adios","nose")