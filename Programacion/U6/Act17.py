'''
Pide al usuario que ingrese un rango (mínimo y máximo) y genera un número aleatorio en ese rango.
●      Captura excepciones si los valores no son numéricos.
●      Asegúrate de que el número mínimo no sea mayor que el máximo.
'''
import random

def generar_numero_aleatorio():
    try:
        minimo = int(input("Ingresa el valor mínimo del rango: "))
        maximo = int(input("Ingresa el valor máximo del rango: "))

        if minimo > maximo:
            raise ValueError()


    except ValueError:
        print("El valor dado no es un numero")

    numero = random.randint(minimo, maximo)
    print(f"Número aleatorio generado entre {minimo} y {maximo}: {numero}")

# Ejecutar el programa
generar_numero_aleatorio()
