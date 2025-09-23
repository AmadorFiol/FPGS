'''
Escribe un programa que pida una fecha en formato dd/mm/yyyy y la convierta en un objeto datetime.
●      Captura errores si el usuario ingresa una fecha inválida (ejemplo: 32/13/2025).
●      Muestra la fecha en diferentes formatos (dd-mm-yyyy, yyyy/mm/dd).
'''
from datetime import datetime

def convertir_fecha():
    fecha_input = input("Ingresa una fecha en formato dd/mm/yyyy: ")
    
    try:
        fecha_objeto = datetime.strptime(fecha_input, "%d/%m/%Y")
        
        print("Fecha original:", fecha_input)
        print("Formato dd-mm-yyyy:", fecha_objeto.strftime("%d-%m-%Y"))
        print("Formato yyyy/mm/dd:", fecha_objeto.strftime("%Y/%m/%d"))
    
    except ValueError:
        print("Error: La fecha ingresada no es válida. Asegúrate de usar el formato dd/mm/yyyy y que sea una fecha real.")

convertir_fecha()
