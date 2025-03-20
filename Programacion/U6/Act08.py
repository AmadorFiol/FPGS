'''
Escribe un programa que intente convertir una cadena en un número.
Si la cadena no se puede convertir en un número, captura la excepción
y muestra un mensaje de error
'''
#string="1"
string="Hola"
try:
   num=int(string)
   print("Se ha podido transfromar el string a un numero")
except:
   print("No se puede transformar el string a un numero") 