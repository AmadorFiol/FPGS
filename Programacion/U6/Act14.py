'''
Desarrolla un sistema de autenticación en el que:
●      El usuario tiene tres intentos para ingresar la contraseña correcta.
●      Si supera los intentos, se lanza una excepción personalizada bloqueando el acceso.
●      Usa un try-except para capturar entradas inválidas.
'''


class AccesoBloqueado(Exception):
    def __init__(self, mensaje="Acceso bloqueado por superar el número de intentos."):
        super().__init__(mensaje)

def sistema_autenticacion():
    contraseña_correcta = "clave123"
    intentos_restantes = 3

    while intentos_restantes > 0:
        try:
            entrada = input("Ingresa la contraseña: ")

            if entrada == contraseña_correcta:
                print("¡Acceso concedido!")
                return
            else:
                intentos_restantes -= 1
                print(f"Contraseña incorrecta. Intentos restantes: {intentos_restantes}")

        except ValueError as e:
            print(f"Error de entrada: {e}")

    raise AccesoBloqueado()

try:
    sistema_autenticacion()
except AccesoBloqueado:
    print("Se han hecho demasiados intentos")
