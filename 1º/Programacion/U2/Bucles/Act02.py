#Crear bucle while que pida un nombre al que saludar o, si el nombre coinicide con el de uno mismo, despedirse
tuNombre=input("Cual es tu nombre? ")
nombre=""
while(nombre!=tuNombre):
    nombre=input("Dime un nombre ")
    print("Hola",nombre)
print("Adios",nombre)