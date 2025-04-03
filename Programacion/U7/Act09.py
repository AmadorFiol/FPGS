'''
Implementa una función llamada `construir_oracion` que reciba
palabras clave (**kwargs) donde cada clave representa una posición
en la oración (ejemplo: primera, segunda, tercera) y devuelva la
oración completa en forma de string.
'''

def construir_oracion(**kwargs):
    oracion=(f"{kwargs["primera"]} {kwargs["segunda"]} {kwargs["tercera"]}")
    return oracion
    

print(construir_oracion(primera="Hola",tercera="Amador",segunda="soy"))
