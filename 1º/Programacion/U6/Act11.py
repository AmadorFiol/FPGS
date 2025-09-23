'''
Crea un programa que simule un cajero automático.
●      Pide al usuario que ingrese su saldo inicial y el monto a retirar.
●      Si el saldo es insuficiente, muestra un mensaje de error.
●      Si el usuario ingresa un valor no numérico, captura la excepción.
●      Asegúrate de que el usuario no retire valores negativos o nulos.
'''

def cajero_automatico():
    try:
        saldo = int(input("Ingresa tu saldo inicial: "))
        if saldo < 0:
            print("El saldo inicial no puede ser negativo.")
            return
        
        retiro = int(input("Ingresa el monto a retirar: "))
        
        if retiro <= 0:
            print("El monto a retirar debe ser mayor que cero.")
        elif retiro > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= retiro
            print(f"Retiro exitoso. Tu nuevo saldo es: ${saldo}")
    
    except ValueError:
        print("Error: Por favor ingresa solo valores numéricos.")

cajero_automatico()
