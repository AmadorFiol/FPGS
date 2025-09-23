'''
Pide al usuario que ingrese una lista de números separados por comas. Luego, el programa deberá dividir cada número por su índice en la lista.
●      Maneja la excepción si el índice es cero.
●      Captura errores si algún valor ingresado no es un número.
●      Evita divisiones entre cero.
'''
def division_entre_indice():
    entrada = input("Ingresa una lista de números separados por comas: ")
    numeros = entrada.split(",")

    for i, num in enumerate(numeros):
        try:
            numero=int(num)
            resultado = numero / i
            print(f"{numero} dividido por su índice {i} es: {resultado}")
        
        except ValueError:
            print(f"Error: '{num}' no es un número válido.")
        except ZeroDivisionError as e:
            print("No se puede dividir entre 0")
        except Exception as e:
            print(f"Ocurrió un error inesperado en el índice {i}: {e}")


division_entre_indice()
