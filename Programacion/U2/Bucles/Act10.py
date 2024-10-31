num=int(input("Dime un numero: "))
factorial=num
for i in range(1,num):
    factorial=factorial*i
print("El factorial de",num," es",factorial)