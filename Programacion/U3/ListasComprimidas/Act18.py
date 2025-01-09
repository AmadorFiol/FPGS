'''
Usando diccionarios comprimidos
Dada una cadena de texto, crea un diccionario que cuente el número de veces que aparece cada vocal en la cadena.
ej frase "hello world"
{'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}.
'''

vocales="aeiou"

frase=input("Escribe una frase ")

diccionario={vocal:frase.lower().count(vocal) for vocal in vocales}
print(diccionario)