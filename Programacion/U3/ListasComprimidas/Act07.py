#Crear una lista de las palabras que comiencen con la letra "a" de una frase.
frase="Ahora esta frase sera dividida y almacenada en una lista"
palabras=[palabra for palabra in frase.split() if palabra.lower().startswith("a")]
print(palabras)