#Crear una lista comprimida con las vocales del alfabeto utilizando un bucle que recorra un string con todas las letras del alfabeto. 
#Crea la misma versión del programa utilizando el código de carácter del código ASCII→ Actividad 4
import string
array=[char for char in string.ascii_lowercase if char in 'aeiou']
print(array)