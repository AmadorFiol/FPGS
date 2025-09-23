#Crea una función en Python llamada area_triangulo que calcule el área de un triángulo, dada la longitud de la base y su altura.
#La base y la altura serán requeridas por pantalla al usuario.
def Calculate_area_triangulo(base,altura):
    area=base*altura/2
    print("El area de tu triangulo es: ",area)

print("Vamos a calcular el area de un triangulo, pero voy a requerir que me digas su base y altura")
base=int(input("Cual es la base de tu triangulo? "))
altura=int(input("Y cual es su altura? "))

Calculate_area_triangulo(base,altura)
