'''
Crea una función llamada construir_configuracion que reciba parámetros de configuración
como argumentos clave-valor y devuelva un diccionario con estas configuraciones.
'''
def construir_conf(**kwargs):
    configuracion={}
    for clave,valor in kwargs.items():
        configuracion[clave]=valor

    return configuracion

print(construir_conf(debug=True, version="1.0.2", modo="producción"))