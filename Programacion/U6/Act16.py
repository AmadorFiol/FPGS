'''
Pide al usuario un número entero y calcula su factorial.
●      Captura excepciones si el usuario ingresa un número negativo o no entero.
●      Evita desbordamientos si el número es demasiado grande.
'''

def calcular_factorial():
    try:
        numero = int(input("Ingresa un número entero positivo: "))

        if numero < 0:
            raise ValueError()
        elif numero > 1000:
            raise OverflowError()
        
    except ValueError:
        print("El valor dado no es un numero o es negativo")
    except OverflowError as oe:
        print("Intente con un numero mas pequeno")
    
    factorial=numero
    for i in range(1,numero):
        factorial=factorial*i

calcular_factorial()
