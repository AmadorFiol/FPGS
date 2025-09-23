'''
Dada una lista de palabras, crea un diccionario que mapee cada palabra a su longitud usando dict comprehension.
ejemplo:
`words = ["apple", "banana", "cherry", "date", "elderberry"]`
Salida: {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4, 'elderberry': 10}`.
'''
array=["apple", "banana", "cherry", "date", "elderberry"]
diccionario={i:len(i) for i in array}
print(diccionario)