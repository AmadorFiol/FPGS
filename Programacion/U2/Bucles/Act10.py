#Crear bucle for que calcule el factorial de un numero insertado por el usuario

num=int(input("Dime un numero: "))
factorial=num
for i in range(1,num):
    factorial=factorial*i
print("El factorial de",num," es",factorial)