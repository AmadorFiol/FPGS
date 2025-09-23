#Crear bucle for que haga un sumatorio de tantos numeros como quiera el usuario

numsAr=[]
sum=0
j=int(input("Dime cuantos numeros vas a sumar: "))
for i in range(0,j):
    print("Dime el",i+1,"º numero")
    num=int(input())
    numsAr.append(num)

for i in numsAr:
    sum=sum+i

print(sum)