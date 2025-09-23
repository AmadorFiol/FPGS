#Crea una función en Python llamada area_cuadrado que calcule el área de un cuadrado, dada la longitud de la base y su altura.
#La base y la altura serán requeridas por pantalla al usuario.
def Calculate_area_cuadrado(lado):
    area=lado**2
    print("El area de tu cuadrado es: ",area)

print("Vamos a calcular el area de un cuadrado, pero voy a requerir que me digas su base y altura")
lado=int(input("Cual es el larogo de tu cuadrado? "))

Calculate_area_cuadrado(lado)
